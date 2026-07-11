import time
import json
import random
import math
import logging
from datetime import datetime
import paho.mqtt.client as mqtt


# ---------------------------------------------------------
# CONFIGURACIÓ
# ---------------------------------------------------------
BROKER = "localhost"
TOPIC_DATA = "rusc/data"
TOPIC_ALERTS = "rusc/alerts"
SEASON = "summer"  # winter, spring, autumn, summer


# ---------------------------------------------------------
# LOGGING
# ---------------------------------------------------------
logging.basicConfig(
    filename="simulator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------------------------------------------------
# PERFILS DE RUSC
# ---------------------------------------------------------
class BeeHiveProfile:
    def __init__(self, name, activity_factor, weight_factor, sound_factor, temp_internal_base):
        self.name = name
        self.activity_factor = activity_factor
        self.weight_factor = weight_factor
        self.sound_factor = sound_factor
        self.temp_internal_base = temp_internal_base


PROFILES = {
    "fort": BeeHiveProfile("fort", 1.2, 1.1, 1.1, 35.0),
    "debil": BeeHiveProfile("debil", 0.7, 0.8, 0.8, 33.5),
    "agressiu": BeeHiveProfile("agressiu", 1.5, 1.0, 1.6, 35.5),
    "hivern": BeeHiveProfile("hivern", 0.4, 0.9, 0.5, 30.0),
    "estiu": BeeHiveProfile("estiu", 1.3, 1.2, 1.2, 36.0)
}


# ---------------------------------------------------------
# ESDEVENIMENTS
# ---------------------------------------------------------
class BeeHiveEvent:
    def __init__(self, name, handler):
        self.name = name
        self.handler = handler


def event_pluja(data):
    data["activity"] *= 0.6
    data["sound"] *= 0.7
    data["temp_out"] -= 2
    return "rain"


def event_calor_extrema(data):
    data["temp_in"] += 2
    data["sound"] *= 1.4
    data["activity"] *= 1.3
    return "heat_wave"


def event_agitacio(data):
    data["sound"] *= 2.0
    data["activity"] *= 1.8
    data["temp_in"] += 1
    return "agitation"


def event_vespa(data):
    data["activity"] *= 0.5
    data["sound"] *= 1.5
    data["temp_in"] -= 0.5
    return "hornet"


EVENTS = {
    "rain": BeeHiveEvent("rain", event_pluja),
    "heat_wave": BeeHiveEvent("heat_wave", event_calor_extrema),
    "agitation": BeeHiveEvent("agitation", event_agitacio),
    "hornet": BeeHiveEvent("hornet", event_vespa)
}


# ---------------------------------------------------------
# ANOMALIES
# ---------------------------------------------------------
class BeeHiveAnomaly:
    def __init__(self, name, handler):
        self.name = name
        self.handler = handler


def anomaly_swarm(data):
    data["weight"] -= random.uniform(3.0, 8.0)
    data["activity"] *= 1.5
    data["sound"] += 15
    return "swarm"


def anomaly_robbery(data):
    data["weight"] -= random.uniform(0.3, 1.0)
    data["activity"] *= 1.8
    data["sound"] *= 2.0
    return "robbery"


def anomaly_disease(data):
    data["activity"] *= 0.5
    data["sound"] *= 0.6
    data["temp_in"] -= 1
    data["weight"] -= 0.1
    return "disease"


ANOMALIES = {
    "swarm": BeeHiveAnomaly("swarm", anomaly_swarm),
    "robbery": BeeHiveAnomaly("robbery", anomaly_robbery),
    "disease": BeeHiveAnomaly("disease", anomaly_disease)
}


# ---------------------------------------------------------
# MODEL MATEMÀTIC
# ---------------------------------------------------------
class BeeHiveModel:

    @staticmethod
    def circadian(hour):
        return math.sin((2 * math.pi * hour) / 24)

    @staticmethod
    def seasonal(day):
        return math.sin((2 * math.pi * day) / 365)

    @staticmethod
    def noise(sigma=0.3):
        return random.gauss(0, sigma)

    @staticmethod
    def micro_fluctuation(t):
        return 0.05 * math.sin(10 * t)

    @staticmethod
    def slow_drift(t):
        return 0.01 * math.sin(0.1 * t)


# ---------------------------------------------------------
# SIMULADOR OO
# ---------------------------------------------------------
class BeeHiveSimulator:
    def __init__(self, profile_name="fort"):
        self.profile = PROFILES[profile_name]

    def generate(self):
        t = time.time()
        dt = datetime.now()
        hour = dt.hour + dt.minute / 60
        day = dt.timetuple().tm_yday

        circ = BeeHiveModel.circadian(hour)
        season = BeeHiveModel.seasonal(day)

        temp_in = self.profile.temp_internal_base + circ + season + BeeHiveModel.noise(0.2)
        temp_out = 15 + 10 * circ + BeeHiveModel.noise(0.5)
        humidity = 50 + 20 * season + BeeHiveModel.noise(1.0)
        weight = 25 * self.profile.weight_factor + season * 2 + BeeHiveModel.noise(0.3)

        activity = (0.5 + circ + season) * self.profile.activity_factor
        activity += BeeHiveModel.micro_fluctuation(t) + BeeHiveModel.slow_drift(t)

        sound = (0.3 + circ) * self.profile.sound_factor
        sound += BeeHiveModel.noise(0.2)

        data = {
            "timestamp": dt.isoformat(),
            "temp_internal": round(temp_in, 2),
            "temp_external": round(temp_out, 2),
            "humidity_external": round(humidity, 2),
            "weight": round(weight, 2),
            "activity": 1 if activity > 0.4 else 0,
            "sound_level": round(sound, 2),
            "current": round(0.08 + 0.04 * activity, 3),
            "profile": self.profile.name,
            "season": SEASON,
            "hour": dt.hour,
            "event": None
        }

        return data


# ---------------------------------------------------------
# MQTT CLIENT
# ---------------------------------------------------------
class MQTTClient:
    def __init__(self, broker=BROKER, topic=TOPIC_DATA, alert_topic=TOPIC_ALERTS):
        self.client = mqtt.Client()
        self.client.connect(broker, 1883, 60)
        self.topic = topic
        self.alert_topic = alert_topic

    def send(self, data):
        self.client.publish(self.topic, json.dumps(data))

    def alert(self, anomaly_name):
        self.client.publish(self.alert_topic, anomaly_name)


# ---------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------
def main():
    sim = BeeHiveSimulator("fort")
    mqtt_client = MQTTClient()

    while True:
        data = sim.generate()

        # Esdeveniments
        if random.random() < 0.05:
            event_name = random.choice(list(EVENTS.keys()))
            EVENTS[event_name].handler(data)
            data["event"] = event_name
            logging.warning(f"Esdeveniment detectat: {event_name}")

        # Anomalies
        if random.random() < 0.02:
            anomaly_name = random.choice(list(ANOMALIES.keys()))
            ANOMALIES[anomaly_name].handler(data)
            data["event"] = anomaly_name
            logging.error(f"Anomalia detectada: {anomaly_name}")
            mqtt_client.alert(anomaly_name)

        mqtt_client.send(data)
        print(data)
        time.sleep(2)


if __name__ == "__main__":
    main()

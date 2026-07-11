import time
import json
import random
import math
import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "localhost"
TOPIC = "ruscs/data"

# Configuració d'estacionalitat
SEASON = "summer"  # "winter", "spring", "autumn", "summer"

def get_hour_factor():
    """Factor circadià basat en l'hora del dia (0–1)."""
    hour = datetime.now().hour
    # Patró: activitat baixa nit, alta migdia
    return 0.5 + 0.5 * math.sin((hour - 6) / 24.0 * 2 * math.pi)

def get_season_factors():
    """Factors segons estació."""
    if SEASON == "winter":
        return {
            "activity": 0.3,
            "external_temp_base": 5,
            "external_temp_range": 5,
            "nectar_flow": 0.1
        }
    elif SEASON == "spring":
        return {
            "activity": 0.7,
            "external_temp_base": 10,
            "external_temp_range": 10,
            "nectar_flow": 0.7
        }
    elif SEASON == "autumn":
        return {
            "activity": 0.5,
            "external_temp_base": 10,
            "external_temp_range": 8,
            "nectar_flow": 0.4
        }
    else:  # summer
        return {
            "activity": 0.9,
            "external_temp_base": 20,
            "external_temp_range": 10,
            "nectar_flow": 0.8
        }

def random_event():
    """Retorna un event especial o None."""
    events = ["swarm", "heat_wave", "rain", "agitation", None, None, None, None]
    return random.choice(events)

def base_external_temp(season_factors, hour_factor):
    return season_factors["external_temp_base"] + season_factors["external_temp_range"] * hour_factor

def simulate_state():
    hour_factor = get_hour_factor()
    season_factors = get_season_factors()
    event = random_event()

    # Activitat base
    activity_base = season_factors["activity"] * hour_factor

    # Temperatura externa
    temp_external = base_external_temp(season_factors, hour_factor)

    # Temperatura interna (regulada 33–36 °C, però afectada per calor externa i events)
    temp_internal = 34.0 + (temp_external - 25.0) * 0.05  # lleu influència externa
    temp_internal += random.uniform(-0.3, 0.3)

    # Pes base (kg)
    weight_base = 25.0

    # Consum base (A)
    current_base = 0.08 + 0.04 * activity_base

    # So base (dB)
    sound_base = 30 + 30 * activity_base

    # Humitat externa (%)
    humidity_external = 50 + 20 * (1 - hour_factor) + random.uniform(-5, 5)

    # Aplicar events especials
    if event == "swarm":
        activity_base *= 1.5
        sound_base += 15
        weight_base -= random.uniform(3.0, 8.0)  # marxen abelles
    elif event == "heat_wave":
        temp_external += random.uniform(5.0, 10.0)
        temp_internal += random.uniform(1.0, 2.0)
        current_base += 0.05  # més ventilació
        sound_base += 10
    elif event == "rain":
        activity_base *= 0.3
        sound_base -= 10
        humidity_external += 20
    elif event == "agitation":
        activity_base *= 1.4
        sound_base += 20
        current_base += 0.03

    # Correlacions entre sensors
    # Si puja temperatura interna, puja consum i so (ventilació)
    if temp_internal > 35.0:
        current_base += 0.03
        sound_base += 5

    # Si activitat alta, puja pes (entrada de nèctar) i so
    weight_delta = season_factors["nectar_flow"] * activity_base * random.uniform(0.0, 0.2)
    weight = weight_base + weight_delta

    # Clamp de valors
    temp_internal = max(30.0, min(38.0, temp_internal))
    temp_external = max(-5.0, min(45.0, temp_external))
    humidity_external = max(20.0, min(100.0, humidity_external))
    current = max(0.03, min(0.25, current_base))
    sound_level = max(20.0, min(90.0, sound_base))
    activity = 1 if activity_base > 0.4 else 0

    return {
        "weight": round(weight, 2),
        "temp_internal": round(temp_internal, 2),
        "temp_external": round(temp_external, 2),
        "humidity_external": round(humidity_external, 2),
        "sound_level": round(sound_level, 2),
        "activity": activity,
        "current": round(current, 3),
        "event": event,
        "season": SEASON,
        "hour": datetime.now().hour
    }

def main():
    client = mqtt.Client()
    client.connect(BROKER)

    print("Simulació avançada iniciada. Enviant dades al broker MQTT...")
    print(f"Broker: {BROKER} | Topic: {TOPIC}")
    print("Prem Ctrl+C per aturar.\n")

    try:
        while True:
            payload = simulate_state()
            payload["timestamp"] = time.time()
            client.publish(TOPIC, json.dumps(payload))
            print(f"[MQTT] {payload}")
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nSimulació aturada.")

if __name__ == "__main__":
    main()

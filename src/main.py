import time
import yaml
import paho.mqtt.client as mqtt

from hx711 import HX711
import adafruit_dht
import board
import onewire
import ds18x20

from alerts import check_alerts


# -----------------------------
# carregar configuració
# -----------------------------
with open("src/config_example.yaml", "r") as f:
    config = yaml.safe_load(f)

MQTT_HOST = config["mqtt"]["host"]
MQTT_PORT = config["mqtt"]["port"]
TOPIC_BASE = config["mqtt"]["topic_base"]
INTERVAL = config["general"]["interval_seconds"]


# -----------------------------
# inicialitzar sensors
# -----------------------------

# pes (HX711)
hx = HX711(dout_pin=5, pd_sck_pin=4)
hx.set_scale_ratio(config["sensors"]["hx711"]["scale_ratio"])

# temperatura/humitat externa (DHT22)
dht = adafruit_dht.DHT22(board.D4)

# temperatura interna (DS18B20)
ow_bus = onewire.OneWireBus(config["sensors"]["ds18b20"]["pin"])
ds = ds18x20.DS18X20(ow_bus, ow_bus.scan()[0])


# -----------------------------
# inicialitzar MQTT
# -----------------------------
client = mqtt.Client()
client.connect(MQTT_HOST, MQTT_PORT, 60)


# -----------------------------
# funcions de lectura
# -----------------------------
def read_weight():
    try:
        return round(hx.get_weight_mean(10), 2)
    except:
        return None


def read_external_temp_hum():
    try:
        return dht.temperature, dht.humidity
    except:
        return None, None


def read_internal_temp():
    try:
        return ds.temperature
    except:
        return None


# -----------------------------
# bucle principal
# -----------------------------
print("Iniciant monitoratge del rusc...")

while True:
    pes = read_weight()
    temp_ext, hum_ext = read_external_temp_hum()
    temp_int = read_internal_temp()

    # publicar dades
    if pes is not None:
        client.publish(f"{TOPIC_BASE}/pes", pes)

    if temp_int is not None:
        client.publish(f"{TOPIC_BASE}/temperatura_interna", temp_int)

    if temp_ext is not None:
        client.publish(f"{TOPIC_BASE}/temperatura_externa", temp_ext)

    if hum_ext is not None:
        client.publish(f"{TOPIC_BASE}/humitat_externa", hum_ext)

    # alertes
    check_alerts(
        pes=pes,
        temp_int=temp_int,
        temp_ext=temp_ext,
        hum_ext=hum_ext
    )

    time.sleep(INTERVAL)

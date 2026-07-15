Backend del sistema de ruscs intel·ligents
El backend és el nucli del sistema: rep dades dels sensors i del mòdul acústic, processa la informació, genera alertes, guarda sèries temporals i alimenta el dashboard en temps real.

Aquest document descriu l’arquitectura, els mòduls principals, els protocols utilitzats i el flux intern del backend.

🧩 Arquitectura general
El backend està format per diversos components:

Receptor de telemetria física (MQTT)

Receptor acústic (UDP/MQTT)

Decodificador Opus → PCM

Pipeline CRNN per detecció acústica

Normalitzador i etiquetador de dades

Generador d’alertes

Persistència a InfluxDB

API interna per al dashboard Streamlit

📡 Recepció de dades
1. Telemetria física (MQTT)
Els sensors del rusc envien dades al backend via MQTT:

HX711 → pes

DS18B20 → temperatura interna

SHT40 → temperatura i humitat externa

Sensor IR → activitat

INA219 → consum energètic

Format recomanat:

json
{
  "rusc_id": "RUSC_01",
  "pes": 42.7,
  "temp_interna": 35.2,
  "temp_externa": 28.1,
  "humitat": 62.4,
  "activitat": 120,
  "consum": 0.18,
  "timestamp": "2026-07-15T07:51:00Z"
}
2. Telemetria acústica (UDP/MQTT)
L’ESP32 acústic envia:

paquets Opus codificats

a 16 kHz mono

en blocs de 20–40 ms

El backend rep els paquets, els decodifica i genera un buffer PCM per al model CRNN.

🔊 Processament acústic
1. Decodificació Opus
El backend utilitza una llibreria Opus per convertir:

Código
Opus → PCM (float32)
2. Generació d’espectrogrames
FFT 512

finestra Hanning

solapament 50%

normalització min-max

3. Inferència CRNN
El model detecta:

vespa

estrès

enjambrament

soroll anòmal

agitació

Sortida típica:

json
{
  "vespa": 0.87,
  "estrès": 0.22,
  "enjambrament": 0.05
}
🚨 Generació d’alertes
El backend combina:

telemetria física

telemetria acústica

correlacions entre sensors

llindars definits

Exemple d’alerta generada:

json
{
  "rusc_id": "RUSC_01",
  "tipus": "acustica_vespa",
  "severitat": "critica",
  "confiança": 0.87,
  "timestamp": "2026-07-15T07:51:00Z"
}
📦 Persistència a InfluxDB
El backend escriu totes les dades i alertes a InfluxDB:

measurement: telemetria

measurement: acustica

measurement: alertes

Tags utilitzats:

rusc_id

tipus

severitat

sensor

📊 Integració amb el dashboard
El backend exposa una API interna per Streamlit:

/api/telemetria/<rusc_id>

/api/alertes/<rusc_id>

/api/acustica/<rusc_id>

/api/espectrograma/<rusc_id>

El dashboard utilitza aquestes rutes per:

mostrar gràfics en temps real

generar informes PDF

visualitzar alertes

comparar ruscs

🧪 Testing i simulació
El backend inclou eines per:

reproduir àudio sintètic

simular vespa, estrès i enjambrament

injectar dades falses de sensors

validar alertes i correlacions

Aquestes eines estan documentades a simulation.md.

📎 Documents relacionats
hardware.md

wiring.md

software-architecture.md

data-flow.md

simulation.md

acoustic.md

alerts.md

dashboard.md

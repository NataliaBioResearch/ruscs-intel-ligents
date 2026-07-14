Dashboard del Rusc Intel·ligent

Aquest document descriu la configuració completa d’InfluxDB i Grafana per monitorar ruscs intel·ligents amb dades de pes, temperatura, humitat, so, activitat i estat energètic. Inclou arquitectura, configuració, queries Flux i recomanacions de visualització.

🟢 1. Arquitectura de dades

El flux de dades del sistema és:

ESP32 → MQTT/HTTP → InfluxDB → Grafana

L’ESP32 envia mesures del rusc.

Les dades arriben via MQTT o HTTP.

InfluxDB les desa en un bucket.

Grafana les visualitza en dashboards interactius.

🟡 2. Configuració d’InfluxDB

2.1 Crear bucket

Nom recomanat: ruscs

Retenció:

30 dies (estalvi d’espai)

90 dies (històric llarg)

2.2 Crear API Token

Tipus: Read/Write

Nom: ruscs-token

2.3 Estructura de mesures

Mesura

Camps

Tags

pes

valor

rusc_id

temp_interna

valor

rusc_id

temp_externa

valor

rusc_id

humitat_externa

valor

rusc_id

so

rms, freq

rusc_id

activitat

entrades, sortides

rusc_id

energia

voltatge, corrent

rusc_id

🔵 3. Configuració de Grafana

3.1 Afegir data source

Grafana → Configuration

Data sources

Add data source

Selecciona InfluxDB

Omple:

URL: http://localhost:8086

Token: ruscs-token

Organization: default

Bucket: ruscs

3.2 Crear dashboard

Nom recomanat: Rusc Intel·ligent — Monitoratge en temps real

🟣 4. Panels recomanats

4.1 Pes del rusc

Tipus: Time series

Query Flux:

from(bucket: "ruscs")
  |> range(start: -24h)
  |> filter(fn: (r) => r._measurement == "pes")

Útil per detectar:

enjambrament

robatori

collita de mel

4.2 Temperatura interna

Tipus: Gauge + Time series

Rang recomanat:

Verd: 33–36°C

Groc: 30–33°C

Vermell: <30°C o >38°C

4.3 Temperatura i humitat externa

Tipus: Time series dual

Permet correlacionar activitat amb clima.

4.4 Activitat d’abelles

Tipus: Bar chart o Stat

Camps: entrades/minut, sortides/minut

4.5 So del rusc

Tipus: Spectrogram o Time series

Camps: RMS, freq dominant

Permet detectar:

estrès

reina perduda

atac de vespa

4.6 Estat energètic

Tipus: Stat + Time series

Camps: voltatge bateria, corrent consum

🧩 5. Alertes en Grafana

Exemple: temperatura interna baixa

Condició:

temp_interna < 32°C durant 10 minuts

Accions: Email, Telegram, Webhook

Exemple: caiguda sobtada de pes

pes baixa > 1 kg en 5 minuts

🧵 6. Bones pràctiques

Usa alias per identificar cada rusc: rusc_id="A1"

Evita intervals massa curts (<10s) per reduir càrrega

Exporta dashboards com JSON per fer còpies de seguretat

Mantén un dashboard minimalista i clar

📎 Documents relacionats

hardware

wiring

main.py

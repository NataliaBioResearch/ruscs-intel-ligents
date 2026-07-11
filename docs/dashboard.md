# dashboard del rusc intel·ligent
Aquest document explica com configurar InfluxDB i Grafana per visualitzar les dades del rusc intel·ligent: pes, temperatura, humitat, so, activitat i estat energètic. Inclou passos detallats, queries i recomanacions de visualització.

🟢 1. arquitectura de dades
El sistema envia dades via MQTT o HTTP a un servidor que les desa a InfluxDB.
Grafana llegeix aquestes dades i genera dashboards interactius.

Flux:

Código
ESP32 → MQTT/HTTP → InfluxDB → Grafana
🟡 2. configuració d’InfluxDB
2.1 crear bucket
Nom recomanat:

Código
ruscs
Retenció:

30 dies (si vols estalviar espai)

90 dies (si vols històric llarg)

2.2 crear API token
Tipus: Read/Write  
Nom: ruscs-token

2.3 estructura de mesures
Mesura	Camps	Tags
pes	valor	rusc_id
temp_interna	valor	rusc_id
temp_externa	valor	rusc_id
humitat_externa	valor	rusc_id
so	rms, freq	rusc_id
activitat	entrades, sortides	rusc_id
energia	voltatge, corrent	rusc_id


🔵 3. configuració de Grafana
3.1 afegir data source
Grafana → Configuration

Data sources

Add data source

Selecciona InfluxDB

Omple:

URL: http://localhost:8086

Token: ruscs-token

Organization: default

Bucket: ruscs

3.2 crear dashboard
Nom recomanat:

Código
Rusc Intel·ligent — Monitoratge en temps real
🟣 4. panels recomanats
4.1 pes del rusc
Tipus: Time series

Query:

Código
from(bucket: "ruscs")
  |> range(start: -24h)
  |> filter(fn: (r) => r._measurement == "pes")
Útil per detectar:

enjambrament

robatori

collita de mel

4.2 temperatura interna
Tipus: Gauge + Time series

Rang recomanat:

Verd: 33–36°C

Groc: 30–33°C

Vermell: <30°C o >38°C

4.3 temperatura i humitat externa
Tipus: Time series dual

Permet correlacionar activitat amb clima.

4.4 activitat d’abelles
Tipus: Bar chart o Stat

Camps:

entrades/minut

sortides/minut

4.5 so del rusc
Tipus: Spectrogram o Time series

Camps:

RMS

Freq dominant

Permet detectar:

estrès

reina perduda

atac de vespa

4.6 estat energètic
Tipus: Stat + Time series

Camps:

voltatge bateria

corrent consum

🧩 5. alertes en Grafana
Exemple d’alerta: temperatura interna baixa
Condició:

Código
temp_interna < 32°C durant 10 minuts
Accions:

Email

Telegram

Webhook

Exemple d’alerta: caiguda sobtada de pes
Código
pes baixa > 1 kg en 5 minuts
🧵 6. bones pràctiques
Usa alias per identificar cada rusc: rusc_id="A1"

Evita intervals massa curts (<10s) per reduir càrrega

Exporta dashboards com JSON per fer còpies de seguretat

Mantén un dashboard minimalista i clar

📎 documents relacionats
hardware

wiring

main.py

alerts.py

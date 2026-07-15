Alertes del sistema de ruscs intel·ligents
Aquest document descriu el sistema d’alertes del projecte: com es generen, quins tipus existeixen, quins llindars s’utilitzen i com es transmeten al backend, a InfluxDB i al dashboard.

Les alertes provenen de dues fonts principals:

Telemetria física (pes, temperatura, humitat, consum)

Telemetria acústica (CRNN, espectrogrames, detecció de vespa, estrès, agitació)

🐝 Tipus d’alertes
1. Alertes acústiques
Generades pel model CRNN a partir del micròfon INMP441.

Enxam imminent

Patró acústic característic

Augment de soroll intern

Activitat irregular

Atac de vespa

Senyal d’alta freqüència

Patró repetitiu i agressiu

Estrès / agitació

Soroll continu

Vibració elevada

Possible manca de reina o intrusió

Cada alerta inclou:

probabilitat del model

confiança

timestamp

ID del rusc

2. Alertes de pes (HX711)
Caiguda sobtada de pes → possible enjambrament

Increment anòmal → humitat interna o acumulació d’aigua

Pes massa baix → colònia feble o manca d’aliment

Llindars recomanats:

Caiguda > 1.5 kg en 24 h → alerta

Caiguda > 3 kg en 24 h → crítica

3. Alertes de temperatura interna (DS18B20)
<32°C → cria en risc

>38°C → sobreescalfament del rusc

Variacions brusques → intrusió o ventilació anòmala

4. Alertes de temperatura i humitat externa (SHT40)
Humitat > 90% → risc de condensació

Temperatura < 5°C → activitat mínima

Temperatura > 40°C → risc d’estrès tèrmic

Aquestes alertes s’utilitzen per correlacionar activitat i soroll.

5. Alertes d’activitat (Sensor IR)
Activitat molt baixa → colònia feble

Activitat molt alta → enjambrament imminent

Activitat nocturna → intrusió o depredador

6. Alertes de consum (INA219)
Consum elevat → ventilació interna o fallada del sistema

Consum nul → bateria esgotada o fallada del panell solar

Variacions sobtades → cable tallat o curtcircuit

📡 Flux d’alertes
Sensors / ESP32

Envia dades via MQTT o UDP

Algunes alertes simples es generen al dispositiu (ex: caiguda de pes)

Backend

Processa dades

Genera alertes complexes (CRNN, correlacions)

Normalitza i etiqueta alertes

InfluxDB

Guarda alertes amb tags:

rusc_id

tipus

severitat

confiança

Dashboard (Streamlit)

Mostra alertes en temps real

Històric d’alertes

Gràfics de correlació

Exportació a PDF

🧪 Validació d’alertes
El sistema utilitza:

tests de camp (vespa, agitació, ventilació)

simulacions (àudio sintètic, variacions de pes)

dades reals de ruscs monitorats

Cada alerta es valida amb:

precisió

sensibilitat

falsos positius

falsos negatius

🗂️ Format d’una alerta
json
{
  "rusc_id": "RUSC_01",
  "tipus": "acustica_vespa",
  "severitat": "critica",
  "confiança": 0.92,
  "timestamp": "2026-07-15T07:51:00Z",
  "detalls": {
    "freq_max": 3800,
    "energia": 0.87
  }
}
📎 Documents relacionats
hardware.md

wiring.md

software-architecture.md

data-flow.md

simulation.md

backend.md

acoustic.md

dashboard.md

# ruscs-intel-ligents

Sistema IoT per al monitoratge de ruscs basat en ESP32 i sensors ambientals. Permet obtenir dades en temps real sobre l'estat del rusc, detectar anomalies i visualitzar la informació mitjançant dashboards interactius.

Característiques
Monitoratge continu del pes del rusc.
Mesura de temperatura interna i externa.
Control de la humitat ambiental.
Anàlisi del nivell de so.
Detecció d'activitat d'entrada i sortida.
Enviament de dades via MQTT.
Sistema d'alertes automàtiques.
Integració amb InfluxDB i Grafana.
Simulador complet per fer proves sense hardware.
Arquitectura
flowchart TD

subgraph Rusc
HX711[HX711 - Pes]
DS18B20[DS18B20 - Temperatura]
SHT40[SHT40 - Humitat]
INMP441[INMP441 - So]
IR[Sensor IR - Activitat]
end

HX711 --> ESP32
DS18B20 --> ESP32
SHT40 --> ESP32
INMP441 --> ESP32
IR --> ESP32

ESP32 --> MQTT[Broker MQTT]
MQTT --> InfluxDB
MQTT --> Alertes

InfluxDB --> Grafana
Quickstart
1. Clonar el repositori
git clone https://github.com/NataliaBioResearch/ruscs-intel-ligents.git
cd ruscs-intel-ligents
2. Instal·lar dependències
pip install -r requirements.txt
3. Executar la simulació
python simulate.py

El simulador genera dades sintètiques realistes del rusc i les publica en temps real.

4. Obrir el dashboard
python dashboard.py
Simulador

El simulador permet provar el sistema sense necessitat de hardware.

Inclou:

Cicles circadians.
Variacions estacionals.
Correlacions entre sensors.
Esdeveniments especials:
pluja
onades de calor
agitació
possible eixamament

Documentació completa a:

docs/simulation.md
Dashboard

El dashboard mostra en temps real:

Pes del rusc
Temperatura interna
Temperatura externa
Humitat
Nivell de so
Activitat
Consum energètic
Alertes i esdeveniments

Compatible amb dades simulades i amb dades provinents de sensors reals.

Hardware

Components principals:

Component	Funció
ESP32	Controlador principal
HX711	Sensor de pes
DS18B20	Temperatura
SHT40	Humitat
INMP441	Micròfon digital
Sensor IR	Activitat
INA219	Monitoratge energètic

Més informació a:

docs/hardware.md
Estructura del projecte
ruscs-intel-ligents/
├── README.md
├── simulate.py
├── dashboard.py
├── src/
│   ├── main.py
│   ├── alerts.py
│   └── config_example.yaml
├── docs/
│   ├── hardware.md
│   ├── wiring.md
│   ├── data-flow.md
│   ├── software-architecture.md
│   └── simulation.md
├── requirements.txt
└── LICENSE
Estat del projecte
✅ Simulador funcional
✅ Dashboard funcional
✅ Sistema MQTT
✅ Sistema d'alertes
🚧 Firmware ESP32 en desenvolupament
🚧 Integració completa amb hardware real
Documentació
docs/hardware.md
docs/wiring.md
docs/data-flow.md
docs/software-architecture.md
docs/simulation.md
Full de ruta

Millores previstes:

Integració completa dels sensors físics.
Persistència de dades amb InfluxDB.
Dashboards avançats amb Grafana.
Predicció d'anomalies amb aprenentatge automàtic.
Aplicació web per al monitoratge remot.
Llicència

Aquest projecte es distribueix sota la llicència MIT.

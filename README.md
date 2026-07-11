# ruscs-intel-ligents
# ruscs-intel-ligents

Sistema IoT per monitorar ruscs amb ESP32 i sensors de pes, temperatura, humitat, so i activitat. Inclou enviament de dades via MQTT, alertes automàtiques i integració amb InfluxDB i Grafana per anàlisi i visualització.

## 🎯 Objectius

- Monitoratge continu del rusc (pes, temperatura interna/externa, humitat, so, activitat).
- Enviament de dades via MQTT a un servidor o dashboard.
- Sistema d’alertes per detectar anomalies (robatori, enjambrament, malaltia, atac de vespa).
- Integració amb InfluxDB + Grafana per visualització.
- Arquitectura replicable i modular.

## 🧩 Arquitectura del sistema

- Microcontrolador: ESP32
- Sensors: HX711, DS18B20, SHT40, INMP441, sensor IR
- Alimentació: panell solar + bateria LiPo + TP4056 + INA219
- Comunicació: MQTT (Mosquitto) o HTTP (FastAPI)
- Dades: InfluxDB
- Dashboard: Grafana

## 📁 Estructura del repositori

ruscs-intel-ligents/
├─ README.md
├─ simulate.py
├─ dashboard.py
├─ src/
│  ├─ main.py
│  ├─ config_example.yaml
│  └─ alerts.py
├─ docs/
│  ├─ hardware.md
│  ├─ wiring.md
│  ├─ data-flow.md
│  ├─ software-architecture.md
│  └─ simulation.md
├─ requirements.txt
└─ LICENSE

## 🚀 Quickstart (prova el projecte en 1 minut)

Aquest projecte inclou un sistema complet per monitorar ruscs intel·ligents.
Pots provar-lo sense hardware gràcies al simulador avançat i al dashboard.

### 1) Clonar el repositori

git clone https://github.com/NataliaBioResearch/ruscs-intel-ligents.git
cd ruscs-intel-ligents

### 2) Instal·lar dependències

pip install -r requirements.txt

### 3) Executar la simulació (sense hardware)

Genera dades realistes del rusc: cicles diaris, estacionalitat, correlacions i esdeveniments especials.

python simulate.py

Documentació completa: docs/simulation.md

### 4) Obrir el dashboard (visualització en temps real)

python dashboard.py

Documentació: docs/dashboard.md

## 🐝 Simulació avançada del rusc

El simulador genera dades realistes del rusc sense necessitat de hardware.
Modela cicles circadians, estacionalitat, correlacions entre sensors i esdeveniments especials (pluja, calor extrema, agitació, enjambrazó).
Les dades es publiquen via MQTT en temps real i permeten provar el dashboard, el flux de dades i el sistema d’alertes amb un sol comandament.

Documentació completa: docs/simulation.md

## 📊 Dashboard en temps real

El dashboard mostra:

- pes del rusc
- temperatura interna i externa
- humitat
- nivell de so
- activitat
- consum elèctric
- esdeveniments especials

Funciona tant amb dades reals com amb la simulació.

Executar:

python dashboard.py

## 🔧 Execució amb hardware real (opcional)

El projecte està preparat per integrar sensors reals (HX711, DS18B20, SHT40, INMP441, INA219, IR).
El fitxer main.py es pot afegir més endavant quan tinguis el firmware complet.

Documentació hardware: docs/hardware.md

## 📜 Instal·lació

git clone https://github.com/NataliaBioResearch/ruscs-intel-ligents.git
cd ruscs-intel-ligents
pip install -r requirements.txt

## 📄 Llicència

MIT License

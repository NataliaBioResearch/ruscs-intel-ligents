# ruscs-intel-ligents
Sistema IoT per monitorar ruscs amb ESP32 i sensors de pes, temperatura, humitat, so i activitat. Inclou enviament de dades via MQTT, alertes automàtiques i integració amb InfluxDB i Grafana per anàlisi i visualització.

## objectius
- Monitoratge continu del rusc (pes, temperatura interna/externa, humitat, so, activitat).
- Enviament de dades via MQTT a un servidor o dashboard.
- Sistema d’alertes per detectar anomalies (robatori, enjambrament, malaltia, atac de vespa).
- Integració amb InfluxDB + Grafana per visualització.
- Arquitectura replicable i modular.

## arquitectura del sistema
- Microcontrolador: ESP32  
- Sensors: HX711, DS18B20, SHT40, INMP441, sensor IR  
- Alimentació: panell solar + bateria LiPo + TP4056 + INA219  
- Comunicació: MQTT (Mosquitto) o HTTP (FastAPI)  
- Dades: InfluxDB  
- Dashboard: Grafana  

## estructura del repositori
ruscs-intel-ligents/
├─ README.md
├─ src/
│  ├─ main.py
│  ├─ config_example.yaml
│  └─ alerts.py
├─ docs/
│  ├─ hardware.md
│  ├─ wiring.md
│  └─ dashboard.md
├─ requirements.txt
└─ LICENSE

## instal·lació
git clone https://github.com/NataliaBioResearch/ruscs-intel-ligents.git
cd ruscs-intel-ligents
pip install -r requirements.txt

## llicència
MIT License

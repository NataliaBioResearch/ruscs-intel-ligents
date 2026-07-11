# hardware del rusc intel·ligent
Aquest document descriu tot el maquinari necessari per muntar un rusc intel·ligent basat en ESP32, sensors IoT i alimentació solar. Inclou especificacions, recomanacions, esquema conceptual i notes de muntatge.

🔌 Microcontrolador — ESP32
WiFi + Bluetooth

Baix consum

Suport per I2C, ADC, 1-Wire

Ideal per lectura de sensors i enviament MQTT

Alternativa: Raspberry Pi Zero W (més potència, més consum).

⚖️ Pes — HX711 + cèl·lula de càrrega 50–100 kg
Mesura el pes del rusc i la producció de mel

Detecta enjambrament (caiguda sobtada de pes)

L’HX711 amplifica i digitalitza la lectura

Connexió:

DOUT → GPIO 5

SCK → GPIO 4

🌡️ Temperatura interna — DS18B20
Alta precisió

Ideal per mesurar temperatura del niu

Detecta problemes de cria (<32°C)

Connexió:

DATA → GPIO 2

Resistència pull-up 4.7kΩ

🌦️ Temperatura i humitat externa — SHT40
Sensor digital I2C

Mesura condicions ambientals

Ajuda a correlacionar activitat amb clima

Connexió:

SDA → GPIO 21

SCL → GPIO 22

🎤 So i vibració — INMP441
Detecta soroll del rusc

Identifica estrès, intrusió o atac de vespa

Permet anàlisi espectral

Connexió (I2S):

DOUT → GPIO 34

WS → GPIO 25

SCK → GPIO 26

🐝 Activitat d’abelles — Sensor IR
Compta abelles entrant/sortint

Permet estimar activitat i força de la colònia

Detecta reducció d’activitat (malaltia, reina feble)

Connexió:

OUT → GPIO 27

🔋 Alimentació — TP4056 + bateria LiPo + panell solar
Panell solar 6–12V

Bateria LiPo 3000–6000 mAh

TP4056 per càrrega segura

INA219 per monitoratge de consum

🧵 Cablejat i protecció — Bones_pràctiques_cablejat
Tub corrugat

Termo-retràctil

Caixa IP65

Malla anti-vespa opcional

🗂️ Resum del maquinari
Component	Funció	Protocol
ESP32	Control i transmissió	WiFi, I2C, ADC, 1-Wire
HX711	Pes del rusc	ADC
DS18B20	Temp. interna	1-Wire
SHT40	Temp./humitat externa	I2C
INMP441	So/vibració	I2S
Sensor IR	Activitat	Digital
INA219	Telemetria consum	I2C


📎 Documents relacionats
wiring.md

dashboard.md
main.py

alerts.py

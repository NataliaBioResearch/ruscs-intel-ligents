# wiring del rusc intel·ligent
Aquest document descriu totes les connexions elèctriques entre l’ESP32 i els sensors del rusc intel·ligent: pes, temperatura, humitat, so, activitat i alimentació. Inclou protocols, pins recomanats i notes de muntatge.

⚙️ 1. connexions del HX711 (pes)
Protocol: ADC digitalitzat
Funció: lectura de la cèl·lula de càrrega

Pin HX711	Pin ESP32
VCC	3.3V
GND	GND
DT (DOUT)	GPIO 5
SCK	GPIO 4


Notes:

Mantén els cables curts per evitar soroll.

La cèl·lula de càrrega ha d’estar fixada amb cargols i suport rígid.

🌡️ 2. connexions del DS18B20 (temperatura interna)
Protocol: 1-Wire
Funció: temperatura del niu

Pin DS18B20	Pin ESP32
VDD	3.3V
GND	GND
DATA	GPIO 2


Important:

Afegeix una resistència pull-up de 4.7kΩ entre DATA i 3.3V.

🌦️ 3. connexions del SHT40 (temperatura/humitat externa)
Protocol: I2C
Funció: condicions ambientals

Pin SHT40	Pin ESP32
VCC	3.3V
GND	GND
SDA	GPIO 21
SCL	GPIO 22


Notes:

Pots afegir resistències pull-up de 10kΩ a SDA i SCL si el cable és llarg.

🎤 4. connexions del INMP441 (micròfon MEMS)
Protocol: I2S
Funció: so i vibració del rusc

Pin INMP441	Pin ESP32
VDD	3.3V
GND	GND
L/R	GND (mode mono)
DOUT	GPIO 34
WS	GPIO 25
SCK	GPIO 26


Notes:

El micròfon ha d’estar protegit però no tapat.

Evita vibracions externes (fixació amb escuma).

🐝 5. connexions del sensor IR (activitat d’abelles)
Protocol: digital
Funció: comptar abelles entrant/sortint

Pin sensor IR	Pin ESP32
VCC	3.3V
GND	GND
OUT	GPIO 27


Notes:

Col·loca el sensor a l’entrada del rusc.

Ajusta sensibilitat segons llum ambiental.

🔋 6. alimentació i monitoratge
TP4056 (càrrega de bateria)
Pin TP4056	Funció
IN+	Panell solar +
IN-	Panell solar -
BAT+	Bateria +
BAT-	Bateria -


INA219 (monitor de consum)
Protocol: I2C
Pins:

Pin INA219	Pin ESP32
VCC	3.3V
GND	GND
SDA	GPIO 21
SCL	GPIO 22


🧵 7. protecció del cablejat
Tub corrugat per evitar humitat i mossegades.

Termo-retràctil a totes les unions.

PCB o protoboard dins caixa IP65.

Passacables amb junta de goma.

🗂️ 8. resum de connexions
Sensor	Protocol	Pins ESP32
HX711	ADC	GPIO 4, 5
DS18B20	1-Wire	GPIO 2
SHT40	I2C	GPIO 21, 22
INMP441	I2S	GPIO 25, 26, 34
Sensor IR	Digital	GPIO 27
INA219	I2C	GPIO 21, 22

# diagrama ASCII del wiring
<pre>
                        ┌──────────────────────────┐
                        │        Panell Solar      │
                        └──────────────┬───────────┘
                                       │
                                 ┌─────▼─────┐
                                 │  TP4056   │
                                 └─────┬─────┘
                                       │
                              ┌────────▼────────┐
                              │   Bateria LiPo   │
                              └────────┬────────┘
                                       │
                              ┌────────▼────────┐
                              │      ESP32       │
                              └────────┬────────┘
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
   ┌────▼────┐                    ┌────▼────┐                    ┌────▼────┐
   │  HX711  │                    │ DS18B20 │                    │  SHT40   │
   └────┬────┘                    └────┬────┘                    └────┬────┘
        │                              │                              │
   DOUT → GPIO 5                  DATA → GPIO 2                 SDA → GPIO 21
   SCK  → GPIO 4                  4.7kΩ pull-up                 SCL → GPIO 22
        │                              │                              │
        │                              │                              │
   ┌────▼────┐                    ┌────▼─────┐                   ┌────▼─────┐
   │ INMP441 │                    │ Sensor IR│                   │  INA219  │
   └─────────┘                    └──────────┘                   └──────────┘
   DOUT → GPIO 34                 OUT → GPIO 27                  SDA/SCL → I2C
   WS   → GPIO 25
   SCK  → GPIO 26
</pre>

📎 documents relacionats
hardware — llistat complet de maquinari

dashboard — configuració de Grafana

main.py — lectura de sensors

alerts.py — sistema d’alertes

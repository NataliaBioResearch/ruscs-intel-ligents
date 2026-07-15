# Simulació del rusc intel·ligent

El simulador del rusc permet provar el sistema complet sense necessitat de maquinari real. Genera dades acústiques i físiques que imiten el comportament d’un rusc en diferents situacions: vespa, estrès, enjambrament, variacions de pes, temperatura i activitat.

És una eina essencial per validar:

- el backend  
- el model CRNN  
- el flux de dades  
- les alertes  
- el dashboard  

---

## 🎤 Simulació acústica

La simulació acústica genera àudio sintètic que imita:

### 1. Vespa
- Senyal d’alta freqüència (3–4 kHz)  
- Patró repetitiu i agressiu  
- Energia elevada  

### 2. Estrès
- Soroll continu  
- Vibració irregular  
- Augment de volum  

### 3. Enjambrament
- Increment progressiu de soroll  
- Activitat interna elevada  
- Patró característic de moviment massiu  

### 4. Soroll ambiental
- Vent  
- Pluja  
- Ocells  
- Vehicles  

Aquestes fonts es poden combinar per crear escenaris realistes.

---

## 🔊 Generació d’espectrogrames simulats

El simulador pot generar espectrogrames directament:

- FFT 512  
- Finestra Hanning  
- Solapament 50%  
- Normalització min-max  

Això permet provar el model CRNN sense passar per Opus.

---

## 📡 Simulació de telemetria física

El simulador envia dades via MQTT que imiten:

### Pes (HX711)
- Caiguda sobtada → enjambrament  
- Increment → humitat interna  
- Oscil·lacions → moviment del rusc  

### Temperatura interna (DS18B20)
- <32°C → cria en risc  
- >38°C → sobreescalfament  

### Temperatura i humitat externa (SHT40)
- Humitat >90% → risc de condensació  
- Temperatura extrema → estrès  

### Activitat (Sensor IR)
- Activitat baixa → colònia feble  
- Activitat alta → enjambrament imminent  

### Consum (INA219)
- Consum elevat → ventilació interna  
- Consum nul → bateria esgotada  

---

## 🧪 Escenaris de simulació

### 1. Enjambrament
- Caiguda de pes  
- Soroll intern elevat  
- Activitat alta  
- CRNN detecta patró d’enjambrament  

### 2. Atac de vespa
- Senyal acústic de vespa  
- Activitat irregular  
- CRNN detecta vespa >0.75  

### 3. Estrès per calor
- Temp interna >38°C  
- Soroll continu  
- Consum elevat (ventilació)  

### 4. Nit amb intrusió
- Activitat nocturna  
- Soroll anòmal  
- Variacions de consum  

---

## 📦 Format de dades simulades

### Telemetria física (MQTT)

```json
{
  "rusc_id": "SIM_01",
  "pes": 41.2,
  "temp_interna": 37.8,
  "temp_externa": 29.1,
  "humitat": 88.2,
  "activitat": 210,
  "consum": 0.22,
  "timestamp": "2026-07-15T07:51:00Z"
}
Telemetria acústica (UDP)
json
{
  "rusc_id": "SIM_01",
  "opus_data": "<bytes>",
  "timestamp": "2026-07-15T07:51:00Z"
}
🧰 Eines del simulador
El simulador inclou:

generador d’àudio sintètic

generador d’espectrogrames

generador de telemetria física

injecció MQTT i UDP

scripts de prova automatitzats

escenaris predefinits

📎 Documents relacionats
hardware.md

acoustic.md

backend.md

alerts.md

data-flow.md

dashboard.md

# Ruscs Intel·ligents — Documentació del Sistema

Benvingut a la documentació oficial del projecte **Ruscs Intel·ligents**, un sistema complet de monitoratge acústic i físic per a ruscs d’abelles. El projecte combina sensors IoT, processament d’àudio, models d’aprenentatge profund i visualització en temps real per oferir una plataforma robusta de vigilància i anàlisi del rusc.

---

## 🐝 Objectiu del projecte

El sistema permet:

- Monitorar l’estat del rusc en temps real  
- Detectar presència de vespa  
- Identificar estrès, agitació i enjambrament  
- Registrar pes, temperatura, humitat i activitat  
- Generar alertes automàtiques  
- Visualitzar dades en un dashboard interactiu  

---

## 🧩 Components principals

### **1. Maquinari del rusc**
Inclou:

- ESP32  
- HX711 + cèl·lula de càrrega  
- DS18B20  
- SHT40  
- INMP441  
- Sensor IR  
- INA219  
- Panell solar + TP4056  

Documentació:  
- [hardware.md](hardware.md)  
- [wiring.md](wiring.md)

---

### **2. Backend**
El backend rep dades, processa telemetria, genera alertes i escriu a InfluxDB.

Documentació:  
- [backend.md](backend.md)  
- [alerts.md](alerts.md)

---

### **3. Subsistema acústic**
Inclou captura I2S, codificació Opus, espectrogrames i model CRNN.

Documentació:  
- [acoustic.md](acoustic.md)

---

### **4. Flux de dades**
Explica com circula la informació des del rusc fins al dashboard.

Documentació:  
- [data-flow.md](data-flow.md)

---

### **5. Arquitectura del software**
Visió general del disseny intern del sistema.

Documentació:  
- [software-architecture.md](software-architecture.md)

---

### **6. Simulació**
Eines per provar el sistema sense maquinari real.

Documentació:  
- [simulation.md](simulation.md)

---

### **7. Dashboard**
Visualització en temps real amb Streamlit.

Documentació:  
- [dashboard.md](dashboard.md)

---

## 🗂️ Estructura del projecte

docs/
│
├── index.md
├── hardware.md
├── wiring.md
├── backend.md
├── acoustic.md
├── alerts.md
├── data-flow.md
├── software-architecture.md
├── simulation.md
└── dashboard.md

Código

---

## 📬 Contacte i contribució

Aquest projecte està en desenvolupament actiu.  
Les contribucions, millores i proves de camp són benvingudes.

---

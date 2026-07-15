Afegit document backend.md amb la descripció completa del backend del sistema de ruscs intel·ligents.

• Explica l’arquitectura general del backend, incloent els mòduls de recepció de dades, processament, normalització i generació d’alertes.
• Documenta el flux d’entrada de telemetria física (MQTT) i telemetria acústica (UDP/MQTT), així com la gestió de buffers, decodificació Opus i conversió PCM.
• Inclou la integració del model CRNN per a detecció acústica (vespa, estrès, enjambrament) i el pipeline d’inferència.
• Detalla la persistència de dades a InfluxDB, incloent tags, mesures, retenció i estructura de sèries temporals.
• Afegeix la gestió d’alertes, correlacions entre sensors i acústica, i enviament al dashboard Streamlit.
• Serveix com a referència central per al desenvolupament, manteniment i extensió del backend del projecte.

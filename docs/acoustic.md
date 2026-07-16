Subsistema acústic del rusc intel·ligent
El subsistema acústic és responsable de detectar patrons sonors relacionats amb l’estat del rusc: presència de vespa, estrès, agitació, enjambrament o soroll anòmal. Utilitza un micròfon digital INMP441, un pipeline de processament d’àudio i un model CRNN entrenat amb dades reals i simulades.

🎤 Micròfon INMP441
El sensor INMP441 és un micròfon digital I2S amb:

Alta sensibilitat

Soroll propi baix

Ideal per capturar vibracions i sons del rusc

Compatible amb ESP32

Connexió I2S recomanada:

DOUT → GPIO 34

WS → GPIO 25

SCK → GPIO 26

📡 Captura d’àudio
L’ESP32 captura l’àudio a:

16 kHz

Mono

Mostres de 32 bits

Blocs de 20–40 ms

Els blocs es codifiquen amb Opus per reduir consum i ample de banda.

Format del paquet:

json
{
  "rusc_id": "RUSC_01",
  "opus_data": "<bytes>",
  "timestamp": "2026-07-15T07:51:00Z"
}
🔊 Decodificació i preprocessament
El backend converteix:

Código
Opus → PCM (float32)
Després genera un espectrograma:

FFT 512

Finestra Hanning

Solapament 50%

Normalització min-max

Aquest espectrograma és l’entrada del model CRNN.

🧠 Model CRNN
El model CRNN (Convolutional Recurrent Neural Network) detecta:

Vespa

Estrès

Enjambrament

Soroll anòmal

Agitació

Sortida típica:

json
{
  "vespa": 0.87,
  "estrès": 0.22,
  "enjambrament": 0.05,
  "agitacio": 0.41
}
🧠 Model CRNN utilitzat
El sistema utilitza el model acústic CRNN real entrenat amb dades de ruscs monitorats i escenaris simulats.
Aquest model es troba al directori:

Código
models/crnn_real.h5
Aquest model s’integra amb els mòduls del namespace ns_acoustic:

ns_acoustic/crnn_model.py — càrrega del model

ns_acoustic/crnn_inference.py — inferència i preprocessament

ns_acoustic/pipeline_acoustic.py — pipeline complet (features → CRNN → alertes)

📥 Entrada del model
Espectrograma Mel 128×128

Normalitzat min-max

Canal únic (mono)

📤 Sortida del model
Vector de probabilitats per a cada classe acústica:

vespa

estrès

enjambrament

agitació

soroll anòmal

Exemple:

json
{
  "vespa": 0.87,
  "estrès": 0.22,
  "enjambrament": 0.05,
  "agitacio": 0.41
}
🚨 Llindars i deteccions
El backend genera alertes quan:

vespa > 0.75 → alerta crítica

estrès > 0.60 → alerta moderada

enjambrament > 0.50 → alerta preventiva

agitacio > 0.70 → alerta d’intrusió o moviment

Els valors es poden calibrar per rusc.

🧪 Validació acústica
El sistema es valida amb:

Àudio real de ruscs monitorats

Simulacions de vespa i estrès

Soroll ambiental (vent, pluja, ocells)

Dades sintètiques generades amb scripts de simulació

Cada detecció es compara amb:

precisió

sensibilitat

falsos positius

falsos negatius

📎 Documents relacionats
hardware.md

backend.md

alerts.md

data-flow.md

simulation.md

dashboard.md

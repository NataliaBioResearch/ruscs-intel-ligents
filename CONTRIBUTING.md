# 🤝 Contributing Guide

Gràcies per voler contribuir al projecte **Rusc Intel·ligent**.  
Aquest document explica com col·laborar de manera eficient, clara i coherent amb l’estil del repositori.

> 🔗 **Enllaç des del README:**  
> Si estàs llegint això des del README, pots tornar-hi aquí:  
> [Torna al README](README.md)

---

## 📑 Taula de continguts
- [Visió general](#visió-general)
- [Com començar](#com-començar)
- [Estructura del repositori](#estructura-del-repositori)
- [Flux de treball amb Git](#flux-de-treball-amb-git)
- [Estil de codi](#estil-de-codi)
- [Tests](#tests)
- [Pull Requests](#pull-requests)
- [Normes per afegir funcionalitats](#normes-per-afegir-funcionalitats)
- [Roadmap tècnic](#roadmap-tècnic)
- [Codi de conducta](#codi-de-conducta)

---

## 🌐 Visió general

El projecte **Rusc Intel·ligent** combina:
- Simulació OO avançada  
- Dashboard Streamlit en temps real  
- Integració amb MQTT  
- InfluxDB + Grafana  
- Alertes heurístiques i ML  
- IA acústica (futur)  
- Multi-rusc (futur)

L’objectiu és crear una plataforma modular, escalable i científica per monitorar ruscs reals i simulats.

---

## 🚀 Com començar

1. Fes un **fork** del repositori.
2. Clona el teu fork:

```bash
git clone https://github.com/EL_TEU_USUARI/rusc-intel-ligent.git
cd rusc-intel-ligent
Crea un entorn virtual:

bash
python3 -m venv venv
source venv/bin/activate
Instal·la dependències:

bash
pip install -r requirements.txt
📁 Estructura del repositori
text
rusc-intel-ligent/
│
├── simulate.py            # Simulador OO complet
├── dashboard.py           # Dashboard Streamlit
│
├── docs/                  # Documentació
│   ├── dashboard.md       # InfluxDB + Grafana
│   ├── architecture.md
│   ├── api.md
│   └── acoustic.md
│
├── src/
│   ├── main.py            # ESP32 / ingestió real
│   ├── alerts.py          # Alertes heurístiques
│   └── utils.py
│
└── tests/                 # Tests automàtics
🔀 Flux de treball amb Git
1. Crea una branca nova
bash
git checkout -b feature/nom-de-la-millora
2. Fes commits petits i clars
Prefixos recomanats:

feat: nova funcionalitat

fix: correcció d’error

docs: documentació

test: afegir o millorar tests

refactor: millora interna

perf: optimització

ci: canvis a GitHub Actions

Exemple:

bash
feat: afegir suport multi-rusc al simulador
3. Puja la branca
bash
git push origin feature/nom-de-la-millora
4. Obre una Pull Request
Inclou:

Descripció clara

Motivació

Com provar-ho

Captures o logs si cal

🎨 Estil de codi
Python 3.10+

PEP8

Noms en snake_case

Classes en CamelCase

Funcions curtes i modulars

Evitar duplicació de codi

Documentar funcions importants

🧪 Tests
Executar tests
bash
pytest -v
Afegir tests nous
Cada funcionalitat nova ha d’incloure:

tests positius

tests negatius

tests d’errors esperats

Objectiu de cobertura:

text
> 85%
📬 Pull Requests
Les PRs han de:

Ser petites i enfocades

No trencar funcionalitats existents

Incloure tests si cal

Incloure documentació si afecta a l’usuari

Les PRs grans han d’incloure:

Diagrama de flux

Notes de migració

Justificació tècnica

🧩 Normes per afegir funcionalitats
Simulador
No afegir dependències innecessàries

Mantenir el model matemàtic modular

Perfils nous → profiles/

Anomalies noves → anomalies/

Dashboard
Gràfics nous → pestanyes noves

No saturar la UI

Mantenir compatibilitat amb dades reals

InfluxDB
Mesures noves → documentar a docs/dashboard.md

Tags obligatoris: rusc_id

IA acústica
Models → models/acoustic/

Dataset → data/acoustic/

Documentació → docs/acoustic.md

🛣️ Roadmap tècnic
[x] Simulador OO complet

[x] Dashboard Streamlit

[x] Documentació Grafana/InfluxDB

[ ] Multi-rusc

[ ] InfluxDB real

[ ] Alertes ML

[ ] IA acústica

[ ] API REST

[ ] App mòbil

🛡️ Codi de conducta
Aquest projecte promou:

Respecte

Col·laboració

Inclusió

Comunicació clara

No s’accepten:

Comentaris ofensius

Assetjament

Discriminació

Abús de poder

🙌 Gràcies!
Cada contribució fa el projecte més robust, útil i científic.
Estem encantats de rebre millores, idees i correccions.

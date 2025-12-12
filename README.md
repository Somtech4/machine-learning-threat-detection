[![ML Threat Detection](./screenshots/step1_upload_dataset.png)](#)

# Machine Learning Threat Detection Pipeline

**Enterprise-ready SOC ML + Threat Intel + SOAR automation**
Enterprise-ready ML pipeline: Colab-based model training ➔ Splunk lookup ingestion ➔ OTX enrichment ➔ SOAR playbook automation with AI-assisted decisions.

🔗 Related: [Threat Hunting Repository](https://github.com/somtech4/threat-hunting)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-orange.svg)]()
[![Build](https://img.shields.io/badge/build-pending-lightgrey.svg)]()
[![Downloads](https://img.shields.io/badge/Artifacts-downloads-lightgrey.svg)]()

---

## TL;DR

Production-style ML pipeline for detecting DDoS, SQL injection, brute force, malware, and zero-day anomalies.
Includes:

* Google Colab notebook for model training
* Python scripts for preprocessing, scoring, and Splunk lookup exports
* AlienVault OTX integration
* SOAR playbooks with AI-assisted decisioning
* Designed for SOC automation demos, interviews, and enterprise readiness

---

## Repository Structure

* `notebooks/` — Google Colab notebooks
* `src/` — Python modules: preprocessing, training, scoring, OTX integration, Splunk export
* `splunk/` — Dashboards, lookups, saved searches
* `playbooks/` — SOAR automation examples
* `screenshots/` — Demo images & placeholders
* `docs/` — Architecture diagrams, threat models

---

## Architecture & Data Flow

*(Insert diagram: `docs/architecture.png` — recommended 1200×600)*

**Pipeline flow:**
Logs ➔ Splunk ➔ ML lookup join ➔ Correlation ➔ Notable ➔ SOAR ➔ AI decision ➔ Action

---

## Demo Screenshots

![Colab upload] <img width="1440" height="900" alt="csv-upload" src="https://github.com/user-attachments/assets/52e7ac75-57d7-437e-9c9b-af7736133e16" />

![SMOTE results] 
<img width="1440" height="900" alt="Smoting1" src="https://github.com/user-attachments/assets/b78a04e7-2b62-456b-abeb-03d435b282ce" />
<img width="1440" height="900" alt="Smoting" src="https://github.com/user-attachments/assets/9ce03ed7-b5ab-4485-85c1-36a4332f7ab7" />

![Model results]<img width="1440" height="900" alt="XGBoost-Model" src="https://github.com/user-attachments/assets/a925ed7c-4e8a-4a3a-8f13-de46fa994059" />
<img width="1440" height="900" alt="Logic regression" src="https://github.com/user-attachments/assets/985d3923-449c-4570-a887-27d8de188cfa" />
<img width="1440" height="900" alt="Random-Forrester" src="https://github.com/user-attachments/assets/355af5d1-96c8-4ff7-b6e2-8f386cd4dbc8" />


![Dashboard](./screenshots/step4_dashboard.png)

---

## Quickstart

### 1. Environment Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 2. Run Notebook
Open `notebooks/ML_Threat_Detection.ipynb` in Google Colab.

### 3. Export Predictions
python src/splunk_export.py --input results/predictions.csv --output splunk/lookups/processed_threat_data.csv


### 4. Splunk Lookup Setup
| inputlookup ml_threat_lookup
| lookup otx_lookup malicious_ip AS src_ip OUTPUT malicious_ip AS otx_hit
| eval severity = case(
    otx_hit=="True","Critical",
    zero_day_flag=="-1","High",
    ml_prediction!="0","Medium",
    true(),"Low"
)
| where severity!="Low"


## SOAR Playbooks

* `playbooks/ai_threat_response.yml` — AI-assisted analyst decisions
* `playbooks/zero_day_containment.yml` — Zero-day threat containment



## Metrics (Example / placeholders)

* Test F1: 0.86
* OTX match rate: 2.3%
* Average inference: 5ms per event


## Roadmap

* Add CI: pytest + flake8 + notebook execution checks
* Docker container for model inference
* Automated OTX refresh via GitHub Actions
* Demo GIF / video walkthrough
* Expand SOAR playbooks and threat coverage


## Contributing

See `CONTRIBUTING.md`.


## Security

See `SECURITY.md` for responsible disclosure procedures.

---

## Contact

Email: somtoeze21@gmail.com
LinkedIn: www.linkedin.com/in/joshua-eze

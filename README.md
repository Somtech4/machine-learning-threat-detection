
# SIEM: Real-Time ML Threat Detection
This project reflects the kind of detection engineering work I’ve done in SOC environments: improving signal quality, reducing alert fatigue, and supporting reliable incident response.

Key skills demonstrated:
- Feature engineering for security telemetry
- ML-assisted detection (Random Forest)
- Real-time ingestion into Splunk via HEC
- API-driven, SOC-ready architecture
- Clear documentation and reproducibility

  
Recommended review order:
1. `docs/architecture.md`
2. `src/model_training.ipynb`
3. `splunk/ingestion_example.conf`

Live API-powered Random Forest model for DDoS, Brute Force, Web Attack.

- 2.24% false positives
- 93.7% attack recall
- Real-time scoring via FastAPI
- Splunk HEC integration (in progress)

## Live Demo

Available on request or can be run locally following Quick Start.

## Quick Start

1. Clone repo
   
git clone https://github.com/Somtech4/machine-learning-threat-detection.git
cd machine-learning-threat-detection

🔗 Related: [Threat Hunting Repository](https://github.com/somtech4/threat-hunting)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-orange.svg)]()
[![Build](https://img.shields.io/badge/build-pending-lightgrey.svg)]()
[![Downloads](https://img.shields.io/badge/Artifacts-downloads-lightgrey.svg)]()


2. Install

pip install -r requirements.txt

3. Run API locally
uvicorn src.api:app --reload

4. Test
python tests/test_detection.py
text## Repository Structure

- `notebooks/` — Training notebook (New_threat.ipynb)
- `models/` — Trained model and artifacts
- `tests/` — 4 use case tests
- `splunk/` — Future HEC config and lookups

## Results

| Attack Type     | Confidence | Final Label |
|-----------------|------------|-------------|
| DDoS            | 0.99       | DDoS        |
| Brute Force     | 0.98       | Brute Force |
| Web Attack      | 0.96       | Web Attack  |
| Benign          | 0.12       | BENIGN      |
These results were generated using simulated attack traffic and benign baseline data to evaluate detection behavior under controlled SOC-like conditions.

## Model Performance

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/329cfea3-be63-4214-a270-6ccb0f5c6fd9" />


The model achieved high recall while maintaining a low false positive rate,
demonstrating suitability for SOC prioritization rather than raw alerting.


## Architecture Overview

<img width="720" height="405" alt="Architecture" src="https://github.com/user-attachments/assets/70efc2a5-9c4d-49e7-b554-9d54e45a8e02" />

This architecture shows how machine-learning-based threat scoring
can be integrated into existing SIEM workflows without replacing
core SOC tooling.
## Roadmap

- Docker deployment
- Full Splunk HEC integration
- SOAR playbooks
- CI/CD pipeline

## SOC & Detection Engineering Relevance

This project reflects real-world detection engineering practices:
- Enhancing SIEM workflows instead of replacing them
- Improving alert prioritization and analyst efficiency
- Supporting explainable, auditable security decisions
- Enabling automation through APIs and structured outputs

The focus is on **operational usability**, not academic ML performance.

## Threat Model & Detection Scope

This project focuses on detecting high-volume and behavioral attack patterns commonly encountered in SOC environments:

- Credential brute-force attacks
- Volumetric denial-of-service (DDoS) activity
- Web application attack traffic

Detections are aligned with MITRE ATT&CK techniques such as:
- T1110 – Brute Force
- T1499 – Endpoint Denial of Service
- T1190 – Exploit Public-Facing Application

The model is designed to support alert prioritization and analyst triage rather than fully automated blocking.

## Design Decisions & Tradeoffs

- Random Forest chosen for interpretability and stability over deep learning
- Feature engineering prioritized over raw packet/log ingestion to reduce noise
- API-based scoring enables SIEM-agnostic integration
- Model augments SIEM workflows rather than replacing native correlation rules



## Contact

somtoeze21@gmail.com  
LinkedIn: www.linkedin.com/in/joshua-eze


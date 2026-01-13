# Architecture & Design Decisions

## Problem Statement
Traditional SIEMs generate high alert volume with limited prioritization,
leading to analyst fatigue and delayed response.

This project explores how ML-based scoring can improve signal quality
while preserving existing SOC workflows.

## Design Principles
- Do not replace SIEM
- Improve prioritization, not alert volume
- Maintain auditability and explainability
- Keep integration lightweight and API-driven

## Data Flow
1. Raw security telemetry is ingested or simulated
2. Features are engineered for attack-relevant patterns
3. A Random Forest model scores events in real time
4. Scores are forwarded to Splunk via HEC
5. Analysts investigate high-confidence events first

## Why Random Forest?
- Handles non-linear patterns well
- Interpretable compared to deep learning
- Suitable for structured security telemetry

## SOC Relevance
This design mirrors how detection engineering teams
incrementally enhance existing SOC capabilities.

## Mock SIEM Injection Client

This module simulates SIEM event enrichment without requiring
a live Splunk or external HTTP collector.

### Purpose
- Validate ML scoring behavior
- Demonstrate SIEM-style enrichment
- Preserve detection logic independent of infrastructure

### How It Works
1. Generates representative security events
2. Sends them to the ML scoring API
3. Receives risk classification and probability
4. Outputs analyst-readable results

### Run Locally
```bash
docker compose up --build
python siem_simulator/send_events.py

import requests
import time

API = "http://localhost:8000/score"

events = [
    {"Dst Port": 22},
    {"Dst Port": 80, "Flow Duration": 2000},
    {"Flow Duration": 10, "Total Length of Fwd Packets": 900000},
    {"Dst Port": 6666},
    {"Dst Port": 8080},
]

print("Starting SIEM Event Injection Simulation")
print("=" * 70)

for i in range(20):
    response = requests.post(API, json=events[i % len(events)])
    result = response.json()

    status = "✓" if response.status_code == 200 else "✗"

    print(
        f"{status} Event {i+1:02d} | "
        f"Label: {result.get('final_label', 'N/A'):15} | "
        f"Probability: {result.get('attack_probability', 0):.2f}"
    )

    time.sleep(0.5)

print("=" * 70)
print("Simulation complete.")
print("This mimics SIEM enrichment without live Splunk dependency.")

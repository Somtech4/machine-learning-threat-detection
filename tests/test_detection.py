import requests

url = "http://localhost:8000/score"  # change to your ngrok URL when live

flows = [
    {"name": "DDoS", "flow": {"Flow Duration": 8000, "Total Length of Fwd Packets": 40, "Total Length of Bwd Packets": 0, "Protocol": 6, "Src Port": 2222, "Dst Port": 80, "Source Port": 2222, "Destination Port": 80}},
    {"name": "Brute Force", "flow": {"Flow Duration": 600000, "Total Length of Fwd Packets": 600, "Total Length of Bwd Packets": 2400, "Protocol": 6, "Src Port": 54321, "Dst Port": 22, "Source Port": 54321, "Destination Port": 22}},
    {"name": "Web Attack", "flow": {"Flow Duration": 1200, "Total Length of Fwd Packets": 380, "Total Length of Bwd Packets": 0, "Protocol": 6, "Src Port": 12345, "Dst Port": 80, "Source Port": 12345, "Destination Port": 80}},
    {"name": "Benign", "flow": {"Flow Duration": 10000000, "Total Length of Fwd Packets": 3200, "Total Length of Bwd Packets": 8900, "Protocol": 6, "Src Port": 54321, "Dst Port": 443, "Source Port": 54321, "Destination Port": 443}},
]

for case in flows:
    result = requests.post(url, json=case["flow"]).json()
    print(f"{case['name']}: {result}")

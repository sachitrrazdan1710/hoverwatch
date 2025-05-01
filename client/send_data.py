import requests
import os
from datetime import datetime

# 🧠 Set your server URL here
SERVER_URL = "http://127.0.0.1:8000/api"  # Change IP for production
DEVICE_ID = "PC001"  # Or generate per machine if needed

def send_log(log_text: str):
    payload = {
        "device_id": DEVICE_ID,
        "log": log_text,
        "timestamp": datetime.utcnow().isoformat()
    }
    try:
        res = requests.post(f"{SERVER_URL}/logs", json=payload, timeout=5)
        if res.status_code != 200:
            print("❌ Log failed:", res.text)
    except Exception as e:
        print("⚠️ Exception while sending log:", e)

def send_screenshot(image_path: str):
    try:
        with open(image_path, "rb") as img:
            files = {"file": img}
            data = {"device_id": DEVICE_ID}
            res = requests.post(f"{SERVER_URL}/screenshots", data=data, files=files, timeout=10)
            if res.status_code != 200:
                print("❌ Screenshot failed:", res.text)
    except Exception as e:
        print("⚠️ Exception while sending screenshot:", e)

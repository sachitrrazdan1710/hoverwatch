import time
import os
from datetime import datetime
import mss
from send_data import send_screenshot  # ✅ Import the backend uploader

SS_DIR = "screenshots"
os.makedirs(SS_DIR, exist_ok=True)

def capture_screenshot():
    with mss.mss() as sct:
        filename = f"ss_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        filepath = os.path.join(SS_DIR, filename)
        sct.shot(output=filepath)

        # ✅ Send to backend after capture
        try:
            send_screenshot(filepath)
        except Exception as e:
            print(f"⚠️ Screenshot send failed: {e}")

def start_screenshot_loop(interval=60):
    while True:
        capture_screenshot()
        time.sleep(interval)

import time
import os
from datetime import datetime
import mss

SS_DIR = "screenshots"
os.makedirs(SS_DIR, exist_ok=True)

def capture_screenshot():
    with mss.mss() as sct:
        filename = os.path.join(SS_DIR, f"ss_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
        sct.shot(output=filename)

def start_screenshot_loop(interval=60):
    while True:
        capture_screenshot()
        time.sleep(interval)

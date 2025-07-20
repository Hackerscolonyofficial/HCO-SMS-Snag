import os
import re
import subprocess
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ HCO Tool running on port 9089"

def start_cloudflared():
    print("[•] Starting Cloudflared tunnel on port 9089...")

    # Remove old log file
    if os.path.exists("cf.log"):
        os.remove("cf.log")

    # Start Cloudflared with log output redirected
    subprocess.Popen(
        ["cloudflared", "tunnel", "--url", "http://127.0.0.1:9089"],
        stdout=open("cf.log", "w"),
        stderr=subprocess.STDOUT
    )

    # Wait for the log file to generate URL
    for _ in range(20):  # ~10 seconds
        if os.path.exists("cf.log"):
            with open("cf.log", "r") as f:
                content = f.read()
                match = re.search(r"https://[a-z0-9]+\.trycloudflare\.com", content)
                if match:
                    return match.group(0)
        time.sleep(0.5)

    return None

if __name__ == '__main__':
    print("[•] Starting Flask server on port 9089...")
    subprocess.Popen(["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=9089"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    time.sleep(3)  # wait for Flask to start

    public_url = start_cloudflared()
    if public_url:
        print(f"[✓] Public URL: {public_url}")
    else:
        print("[×] Could not retrieve Cloudflared URL.")

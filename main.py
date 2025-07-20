import os
import re
import subprocess
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ HCO Tool is running on port 9089"

def start_cloudflared():
    print("[•] Starting Cloudflared tunnel on port 9089...")
    process = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", "http://127.0.0.1:9089"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )

    # Wait and capture the output
    url = None
    for _ in range(20):  # check output lines for 10 seconds
        line = process.stdout.readline()
        if line == '':
            break
        match = re.search(r"https://[a-z0-9]+\.trycloudflare\.com", line)
        if match:
            url = match.group(0)
            break
        time.sleep(0.5)

    if url:
        print("[•] Cloudflare Tunnel URL:", url)
        return url
    else:
        print("[×] Failed to retrieve Cloudflare URL.")
        return None

if __name__ == '__main__':
    print("[•] Starting Flask server on port 9089...")
    subprocess.Popen(["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=9089"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    time.sleep(4)  # wait for Flask to start

    # Start tunnel
    tunnel_url = start_cloudflared()
    if tunnel_url:
        print(f"[✓] Your Public URL: {tunnel_url}")
    else:
        print("[×] Could not start Cloudflared tunnel.")

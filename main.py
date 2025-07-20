import os
import subprocess
import time
import re
from flask import Flask

app = Flask(__name__)

def start_cloudflared():
    print("[•] Starting Flask server...")
    
    # Start Flask server in background
    subprocess.Popen(["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    time.sleep(3)

    print("[•] Starting Cloudflared tunnel...")
    tunnel_proc = subprocess.Popen(["cloudflared", "tunnel", "--url", "http://127.0.0.1:5000"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    url = None
    for _ in range(10):  # wait up to 10 seconds
        line = tunnel_proc.stdout.readline()
        if line == '':
            break
        match = re.search(r"https://[a-z0-9]+\.trycloudflare\.com", line)
        if match:
            url = match.group(0)
            break

    if url:
        print("[•] Cloudflare Tunnel URL:", url)
        return url
    else:
        print("[×] Failed to get Cloudflare URL. Make sure tunnel started properly.")
        return "[×] Tunnel Error"

@app.route('/')
def home():
    return "✅ HCO Tool Running..."

if __name__ == '__main__':
    tunnel_url = start_cloudflared()
    print("[•] Public URL =>", tunnel_url)

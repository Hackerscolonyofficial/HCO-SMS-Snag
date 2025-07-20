import os
import re
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ HCO Tool is active on port 9089"

def get_cloudflared_url():
    print("[•] Checking for Cloudflare URL from log...")
    try:
        logs = os.popen("logcat -d | grep trycloudflare").read()
        match = re.search(r"https://[a-z0-9]+\.trycloudflare\.com", logs)
        if match:
            return match.group(0)
    except:
        pass
    return "[×] Tunnel not detected. Start it manually."

if __name__ == '__main__':
    print("[•] Make sure you have manually started Cloudflared in another tab.")
    print("[•] Starting Flask server on port 9089...")
    url = get_cloudflared_url()
    print("[•] Cloudflare Tunnel URL:", url)
    app.run(host="0.0.0.0", port=9089)

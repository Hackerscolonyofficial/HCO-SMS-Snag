<h1 align="center">📩 HCO-SMS-Snag</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Termux-black?style=for-the-badge&logo=android" />
  <img src="https://img.shields.io/badge/Made%20By-Azhar-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tool%20Type-SMS%20Logger-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Fully%20Working-green?style=for-the-badge" />
</p>

---

## 🚀 About

**HCO-SMS-Snag** is a Termux-based educational tool that captures SMS messages from a victim's device and displays them live in your terminal. It uses a Flask server and Cloudflare tunneling to create a public link. Victims are asked for permission before data is fetched.

> 🛑 **Note:** This tool is only for **ethical testing**, education, and awareness.

---

## 📲 Termux Setup

Copy-paste the commands below into your Termux terminal:

```bash
# ✅ Update Termux
pkg update -y && pkg upgrade -y

# ✅ Install Python and Git
pkg install python -y
pkg install git -y

# ✅ Install Required Python Libraries
pip install flask requests

# ✅ Clone the Tool
git clone https://github.com/Hackerscolonyofficial/HCO-SMS-Snag.git

# ✅ Navigate to the Tool Directory
cd HCO-SMS-Snag

# ✅ Start the Tool
python main.py
```

---

## 📦 Files Included

- `main.py` – Flask server + Cloudflare + SMS Logger
- `sms.txt` – All collected SMS messages saved here
- `requirements.txt` – Python dependencies list
- `.gitignore` – Hides pycache and unnecessary files
- `README.md` – This full documentation

---

## 🛠️ Requirements

All dependencies are listed in `requirements.txt`:

```txt
flask
requests
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Features

- 📩 Logs victim SMS inbox with permission
- 🔗 Creates public Cloudflare tunnel
- 🎯 Auto YouTube subscription redirect before tool runs
- 📥 Saves all SMS to `sms.txt`
- 🌈 Colorful Termux output (green, red, yellow)
- 🔐 Secure access key built-in

---

## ⚠️ Disclaimer

> This project is intended for **educational purposes** only.  
> You are solely responsible for your actions.  
> **Hackers Colony** and the developer will not be held liable for any misuse.

---

## 👨‍💻 Developer

**🔹 Code by Azhar**  
🎥 [Subscribe on YouTube](https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya)  
📍 Instagram: [@hackers_colony_official](https://www.instagram.com/hackers_colony_official)  
📍 Telegram: [Hackers Colony](https://t.me/hackersColony)

---

## 💬 Final Quote

> 💡 “**Tools can educate or exploit. Choose wisely.**”  
> — Hackers Colony

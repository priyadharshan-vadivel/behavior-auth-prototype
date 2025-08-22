# 🛡️ Behavior-Based Authentication Prototype

Welcome to our hackathon project! 🎉  
This prototype reimagines digital banking security by looking not just at **what you know** (like passwords/OTPs), but at **how you behave** while using an app.  

Instead of asking for codes every time, our system learns your **typing speed, swiping patterns, login habits, and device usage** to spot fraud in real-time.  
If a fraudster tries to log in, the system flags them immediately — even if they somehow stole your password.

---

## ✨ Why This Project?
Online banking fraud is on the rise with **SIM swaps, phishing, and device spoofing**. Traditional security methods like OTPs can be bypassed.  

Our idea is simple:  
👉 **Your behavior is unique.** It’s way harder to fake than a password.  

So, we built a quick **web app prototype** that:  
- Collects behavioral data (keystroke latency, swipe speed, login hour, device info)  
- Runs it through an **ML anomaly detector (Isolation Forest)**  
- Decides if the login is **Genuine ✅, Suspicious 🔒, or Fraud 🚫**  

---

## 🚀 Features
- 🖥️ Streamlit web interface — no command line required  
- 🤖 Machine learning–powered fraud detection  
- 🎯 Risk-based decisions: **Access / Challenge / Block**  
- 📜 Login attempts history (so you can demo multiple sessions)  
- 📈 Interactive anomaly score graph (with fraud threshold)  
- ⚡ Lightweight & hackathon-ready  

---

## 🛠️ Installation & Setup

### 1. Clone this repo
```bash
git clone https://github.com/priyadharshan-vadivel/behavior-auth-prototype.git
cd behavior-auth-prototype
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the web app
```bash
python -m streamlit run app.py
```

Your browser will open automatically at 👉 http://localhost:8501

---

## 🎮 How to Demo (Hackathon Flow)

Here’s a fun way to show it live:

### 🟢 Legit User
- Keystroke latency: 220  
- Swipe speed: 950  
- Login hour: 14  
- Device change: 0  
➡️ **Result:** ✅ Access Granted

### 🔴 Fraudster
- Keystroke latency: 800  
- Swipe speed: 400  
- Login hour: 2  
- Device change: 1  
➡️ **Result:** 🚫 Block Access

### 🟡 Suspicious Case
- Keystroke latency: 350  
- Swipe speed: 700  
- Login hour: 20  
- Device change: 0  
➡️ **Result:** 🔒 Challenge User  

---

## 📊 Visuals
- **Login History Log** → shows all attempts in a table  
- **Anomaly Score Graph** → red line = fraud threshold  

This helps judges see the **AI in action**, not just text outputs.

---

## 📦 requirements.txt
```txt
pandas
scikit-learn
streamlit
matplotlib
```

---

## 🎤 Pitch This in a Hackathon
“Passwords and OTPs are no longer enough. Attackers bypass them using SIM swaps and phishing.  
But your typing rhythm, swipe gestures, and login behavior are much harder to fake.  

Our prototype continuously authenticates users based on **what they do, not just what they know**.  
That means **seamless security for real users** and **instant fraud detection** for attackers.”

---

## 📜 License
Open-source and free for hackathon & educational use. 🚀

---

👨‍💻 Built with love, coffee, and late-night debugging.

# 🛡️ DDoS Protection System for Cloud  
A security-oriented project built with **Python** to detect and mitigate Distributed Denial-of-Service (DDoS) attacks using custom firewall rules, logging, and automated protection.  

---

## 🚀 Features
- 🔍 **Real-time Traffic Monitoring** – Detect suspicious packets.  
- 🔒 **Automatic Blocking** – Blocks malicious IPs dynamically.  
- 📜 **Logging System** – Tracks attack attempts in `firewall.log`.  
- ⚡ **Custom Rules** – Add/Remove firewall rules via GUI/CLI.  
- 🌐 **Cross-Platform** – Works with Linux/Kali & Windows (using iptables/Windows Firewall).  

---

## 🛠️ Tech Stack
- **Language:** Python 3  
- **Libraries/Tools:**  
  - `socket`, `threading`, `subprocess`  
  - `tkinter` (GUI)  
  - `iptables` / `netsh advfirewall`  
- **Platform:** Windows / Linux (Kali recommended)  

---

## 📂 Project Structure
ddos-protection-system/
│── main.py # Entry point
│── firewall.py # Core firewall logic
│── gui.py # GUI for managing firewall
│── requirements.txt # Dependencies
│── README.md # Documentation
│── firewall.log # Logs of blocked IPs
│── .gitignore # Ignore unnecessary files

---

## ⚙️ Installation & Usage
### 🔹 1. Clone the Repository
```bash
git clone https://github.com/Sandipan2011/ddos-protection-system.git
cd ddos-protection-system

---

##Install Requirements
pip install -r requirements.txt

---

##Run the System
python main.py

---

##Future Improvements
AI-based Threat Scoring system 🧠
GeoIP Detection 🌍
Advanced Web Dashboard for live monitoring 📈

##Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

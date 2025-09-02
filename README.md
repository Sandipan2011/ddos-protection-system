# 🛡️ DDoS Protection System for Cloud  
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

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

## 🛠️ Languages Used

This project is built using **1 programming language**:

- **Python 3** - The primary language for the entire codebase, including core logic, deployment scripts, and cloud integrations.

---

## 📂 Project Structure
```
D-D-O-S PROTECTION SYSTEM/
├── deploy_aws.py          # AWS deployment script
├── deploy_azure.py        # Azure deployment script
├── deploy_gcp.py          # GCP deployment script
├── main.py                # Entry point
├── README.md              # Documentation
├── requirements.txt       # Dependencies
├── test_ddos.py           # Test script
├── logs/
│   └── firewall.log       # Logs of blocked IPs
└── src/
    ├── __init__.py
    ├── blockchain_integration.py
    ├── cloud_protection/
    │   ├── __init__.py
    │   ├── aws_protection.py
    │   ├── azure_protection.py
    │   └── gcp_protection.py
    ├── firewall/
    │   ├── __init__.py
    │   └── firewall.py
    └── selfhealing/
        ├── __init__.py
        └── selfhealing.py

mod-ddos-protection-system/
├── firewall.exe
├── logs/
│   └── firewall.log
└── src/
    ├── firewall/
    │   ├── firewall.exe
    │   └── ultra-secure-firewall.exe
    └── selfhealing/
```

---

## ⚙️ Installation & Usage
### 🔹 1. Clone the Repository
```bash
git clone https://github.com/Sandipan2011/ddos-protection-system.git
cd "D-D-O-S PROTECTION SYSTEM"
```

### 🔹 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 🔹 3. Run the System
```bash
python main.py
```

---

## 🚀 Future Improvements
AI-based Threat Scoring system 🧠
GeoIP Detection 🌍
Advanced Web Dashboard for live monitoring 📈

##Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

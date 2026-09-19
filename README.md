# 🛡️ DDoS Protection System for Cloud

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/AWS%20%7C%20Azure%20%7C%20GCP-Cloud%20Protection-232F3E?style=for-the-badge" alt="Cloud Protection" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-10B981?style=for-the-badge" alt="Supported platforms" />
  <img src="https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge" alt="MIT License" />
</p>

<p align="center">
  A Python-based defensive security prototype for monitoring suspicious traffic, managing firewall rules, and automating DDoS response workflows.
</p>

> **Important:** This project is intended for authorized defensive security, learning, and controlled testing environments. Do not use it to interfere with networks or systems without permission.

---

## Overview

The DDoS Protection System for Cloud is a security-oriented Python project that combines traffic monitoring, automated IP blocking, firewall rule management, event logging, and cloud-specific protection modules.

It is designed as a practical prototype for exploring how a defensive network protection workflow can detect suspicious activity and respond through platform-native firewall controls.

---

## Features

- **Traffic monitoring** — Inspect traffic patterns and identify suspicious activity.
- **Automated blocking** — Dynamically block addresses identified as malicious.
- **Firewall management** — Add and remove custom rules through supported system tools.
- **Security logging** — Record protection events and blocked addresses in `firewall.log`.
- **Cloud modules** — Include separate protection integrations for AWS, Azure, and Google Cloud.
- **Self-healing foundation** — Provide a starting point for automated recovery and protection workflows.
- **Cross-platform direction** — Support Linux/Kali through `iptables` and Windows through `netsh advfirewall`.
- **Optional GUI tooling** — Use Tkinter-based interfaces where available.

---

## Architecture

```text
D-D-O-S PROTECTION SYSTEM/
├── deploy_aws.py                 # AWS deployment entry point
├── deploy_azure.py               # Azure deployment entry point
├── deploy_gcp.py                 # Google Cloud deployment entry point
├── main.py                       # Application entry point
├── requirements.txt              # Python dependencies
├── test_ddos.py                  # DDoS protection tests
├── logs/
│   └── firewall.log              # Firewall and protection events
└── src/
    ├── blockchain_integration.py
    ├── cloud_protection/
    │   ├── aws_protection.py
    │   ├── azure_protection.py
    │   └── gcp_protection.py
    ├── firewall/
    │   └── firewall.py
    └── selfhealing/
        └── selfhealing.py
```

The repository also contains `mod-ddos-protection-system/`, which stores packaged firewall-related binaries and supporting runtime files.

---

## Technology stack

- **Language:** Python 3.8+
- **Standard libraries:** `socket`, `threading`, and `subprocess`
- **Interface:** Tkinter GUI support where configured
- **Linux firewall:** `iptables`
- **Windows firewall:** `netsh advfirewall`
- **Cloud targets:** AWS, Azure, and Google Cloud
- **License:** MIT

---

## Requirements

Before running the project, make sure you have:

- Python 3.8 or newer
- Administrator/root privileges for firewall operations
- The appropriate firewall tooling for your operating system
- Cloud credentials configured if using a cloud deployment module
- Permission to monitor and modify the target system

Firewall commands can change system networking behavior. Test in a disposable or controlled environment first.

---

## Installation

```bash
git clone https://github.com/Sandipan2011/ddos-protection-system.git
cd ddos-protection-system
python -m venv .venv
```

### Activate the virtual environment

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Usage

Run the main application from an authorized environment:

```bash
python main.py
```

Run the available tests:

```bash
python test_ddos.py
```

Depending on the operating system and selected protection mode, the application may need to be launched with elevated privileges.

### Cloud deployment modules

The repository includes separate entry points for cloud-specific workflows:

```bash
python deploy_aws.py
python deploy_azure.py
python deploy_gcp.py
```

Review each deployment script and configure credentials, permissions, regions, and target resources before execution. Never commit cloud secrets to the repository.

---

## Logging

Protection events are written to:

```text
logs/firewall.log
```

Use the log to review blocked addresses, firewall actions, and detection events. In production-like environments, configure log rotation, access controls, and centralized monitoring before generating high-volume traffic logs.

---

## Roadmap

Planned improvements include:

- AI-assisted threat scoring
- GeoIP enrichment
- A live monitoring dashboard
- More robust rate limiting and threshold configuration
- Better cloud-provider abstractions
- Expanded automated tests and safer dry-run modes
- Structured logging and alert integrations

---

## Responsible use

This project can make system-level firewall changes and may block network addresses automatically. Use it only on systems and networks you own or are explicitly authorized to protect.

For safe development and testing:

- Prefer a dry-run mode before enabling blocking.
- Use synthetic traffic and isolated test environments.
- Keep an administrative recovery path available.
- Validate rules before applying them to production systems.
- Avoid storing credentials or sensitive traffic data in logs.

---

## Contributing

Contributions are welcome. For substantial changes, open an issue first to discuss the proposed design. Pull requests should include relevant tests and explain any changes to firewall behavior or cloud permissions.

---

## License

This project is released under the [MIT License](LICENSE).

<p align="center">
  Built for authorized defensive security research and experimentation.
</p>

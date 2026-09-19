# 🛡️ DDoS Protection System

A security-focused Python project designed to detect, monitor, and mitigate Distributed Denial-of-Service (DDoS) attacks using firewall automation, threat logging, and cloud-aware protection workflows.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/) [![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)](https://github.com/Sandipan2011/ddos-protection-system) [![License](https://img.shields.io/badge/license-MIT-green.svg)](../LICENSE)

---

## Overview

This project provides a practical foundation for building a DDoS defense layer in cloud and local environments. It combines IP monitoring, custom firewall rules, event logging, and automatic mitigation logic to help detect suspicious traffic and block malicious endpoints before they overwhelm the target system.

The system is built to work across Linux and Windows environments and includes deployment modules for major cloud providers such as AWS, Azure, and Google Cloud Platform.

---

## Features

- Real-time packet and traffic monitoring
- Dynamic blocking of suspicious or malicious IP addresses
- Logging of attack attempts to `firewall.log`
- Firewall rule management using system-native tools
- Cloud-specific protection hooks for AWS, Azure, and GCP
- Self-healing and protection workflow integration
- Cross-platform support for Linux and Windows
- Lightweight Python-based architecture for rapid extension

---

## Architecture

The project is organized into a few core modules:

- `main.py` — application entry point
- `src/firewall/` — firewall logic and rule enforcement
- `src/selfhealing/` — automated remediation and recovery logic
- `src/cloud_protection/` — cloud provider threat mitigation modules
- `src/blockchain_integration.py` — optional blockchain-related integration logic
- `logs/` — generated attack logs and monitoring output

This modular design makes it easier to add or replace protection strategies without changing the full application flow.

---

## Tech Stack

- Python 3.8+
- `socket`
- `threading`
- `subprocess`
- `tkinter` (GUI support)
- `iptables` for Linux
- `netsh advfirewall` for Windows
- Cloud APIs and deployment automation for AWS, Azure, and GCP

---

## Project Structure

```text
DDoS Protection System/
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
├── test_ddos.py
├── deploy_aws.py
├── deploy_azure.py
├── deploy_gcp.py
├── logs/
│   └── firewall.log
├── src/
│   ├── __init__.py
│   ├── blockchain_integration.py
│   ├── cloud_protection/
│   │   ├── __init__.py
│   │   ├── aws_protection.py
│   │   ├── azure_protection.py
│   │   └── gcp_protection.py
│   ├── firewall/
│   │   ├── __init__.py
│   │   └── firewall.py
│   └── selfhealing/
│       ├── __init__.py
│       └── selfhealing.py
├── mod-ddos-protection-system/
│   ├── firewall.exe
│   ├── logs/
│   │   └── firewall.log
│   └── src/
│       ├── firewall/
│       │   ├── firewall.exe
│       │   └── ultra-secure-firewall.exe
│       └── selfhealing/
└── TODO_*.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sandipan2011/ddos-protection-system.git
cd ddos-protection-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python main.py
```

---

## Usage

Once the application starts, it will:

1. Begin monitoring traffic patterns
2. Detect suspicious request bursts or abnormal behavior
3. Identify malicious source IPs
4. Apply firewall rules to block hostile traffic
5. Log blocked attempts for review and analysis

This can serve as a base for experimentation, local security testing, or as a starting point for a larger cloud defense platform.

---

## Cloud Deployment

The repository includes deployment entry points for major cloud providers:

- `deploy_aws.py` for AWS-based deployment
- `deploy_azure.py` for Azure deployment
- `deploy_gcp.py` for Google Cloud deployment

These scripts help extend the protection layer into cloud-managed environments and are useful for rapid proof-of-concept deployments.

---

## Security Considerations

This project is intended for defensive monitoring and educational use. Before deploying it in production, consider:

- validating firewall rules in a safe environment
- testing on a non-production system first
- implementing rate-limit and anomaly detection logic tuned to your environment
- restricting privileges for automation and cloud deployment tasks

---

## Roadmap

Planned improvements include:

- AI-based threat scoring
- GeoIP and geographic risk analysis
- Real-time dashboard with monitoring metrics
- Expanded anomaly detection models
- Better integration with cloud-native security tooling

---

## Contributing

Contributions are welcome. For significant changes, please open an issue first to discuss the direction of the update before submitting a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

---

## Maintainer

Built and maintained by the project author and contributors in the [Sandipan2011/ddos-protection-system](https://github.com/Sandipan2011/ddos-protection-system) repository.


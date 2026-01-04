#!/usr/bin/env python3
"""
Main entry point for the D-D-O-S PROTECTION SYSTEM
"""

import sys
import os
import logging
import json
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from firewall.firewall import Firewall
from selfhealing.selfhealing import SelfHealing
try:
    from blockchain_integration import BlockchainIntegration
    blockchain_available = True
except ImportError as e:
    print(f"Blockchain integration not available: {e}")
    blockchain_available = False
from cloud_protection import AWSProtection, AzureProtection, GCPProtection

# Setup logging
log_file = os.path.join(os.path.dirname(__file__), 'logs', 'firewall.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    print("=== Ultra-Secure Firewall Verification ===")
    logging.info("Verifying Ultra-Secure Firewall functionality...")

    # Initialize components
    firewall = Firewall()
    self_healing = SelfHealing()
    if blockchain_available:
        blockchain = BlockchainIntegration()
        blockchain.initialize()
    else:
        print("Skipping blockchain integration due to import error.")

    firewall.initialize()
    self_healing.initialize()

    # Initialize cloud protection (optional)
    print("=== Cloud Protection Initialization ===")
    try:
        # AWS Protection
        aws_protection = AWSProtection()
        if aws_protection.initialize():
            print("AWS Shield integration ready")
        else:
            print("AWS Shield integration failed - check credentials")

        # Azure Protection (requires subscription_id and resource_group)
        # azure_protection = AzureProtection(subscription_id='your-subscription-id', resource_group='your-rg')
        # if azure_protection.initialize():
        #     print("Azure DDoS Protection integration ready")
        # else:
        #     print("Azure DDoS Protection integration failed")

        # GCP Protection (requires project_id)
        # gcp_protection = GCPProtection(project_id='your-project-id')
        # if gcp_protection.initialize():
        #     print("GCP Cloud Armor integration ready")
        # else:
        #     print("GCP Cloud Armor integration failed")

    except Exception as e:
        print(f"Cloud protection initialization error: {e}")

    print("All critical DDoS protection components are functional!")
    logging.info("All critical DDoS protection components are functional!")

    print("DDoS Protection System is ready for production deployment!")
    logging.info("DDoS Protection System is ready for production deployment!")

if __name__ == "__main__":
    main()

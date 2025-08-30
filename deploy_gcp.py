#!/usr/bin/env python3
"""
GCP Deployment Script for DDoS Protection System
Deploys GCP Cloud Armor protections
"""

import sys
import os
import argparse

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from cloud_protection.gcp_protection import GCPProtection

def main():
    parser = argparse.ArgumentParser(description='Deploy GCP DDoS Protection')
    parser.add_argument('--project-id', required=True, help='GCP project ID')
    parser.add_argument('--policy-name', default='ddos-protection-policy', help='Security policy name')
    parser.add_argument('--backend-service', help='Backend service name to protect')
    parser.add_argument('--region', default='us-central1', help='GCP region')

    args = parser.parse_args()

    gcp_protection = GCPProtection(project_id=args.project_id)

    if not gcp_protection.initialize():
        print("Failed to initialize GCP protection")
        return

    print(f"Creating Cloud Armor security policy: {args.policy_name}")
    policy_name = gcp_protection.create_security_policy(args.policy_name)
    if policy_name:
        print(f"Security policy created: {policy_name}")
    else:
        print("Failed to create security policy")

    if args.backend_service:
        print(f"Attaching policy to backend service: {args.backend_service}")
        if gcp_protection.attach_policy_to_backend(args.policy_name, args.backend_service, args.region):
            print("Policy attached successfully")
        else:
            print("Failed to attach policy")

    print("Adding rate limiting rule...")
    if gcp_protection.create_rate_limit_rule(args.policy_name):
        print("Rate limiting rule added")
    else:
        print("Failed to add rate limiting rule")

    print("GCP deployment completed")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
AWS Deployment Script for DDoS Protection System
Deploys AWS Shield and WAF protections
"""

import sys
import os
import argparse

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from cloud_protection.aws_protection import AWSProtection

def main():
    parser = argparse.ArgumentParser(description='Deploy AWS DDoS Protection')
    parser.add_argument('--region', default='us-east-1', help='AWS region')
    parser.add_argument('--resource-arn', help='ARN of resource to protect')
    parser.add_argument('--enable-advanced', action='store_true', help='Enable Shield Advanced')

    args = parser.parse_args()

    aws_protection = AWSProtection(region=args.region)

    if not aws_protection.initialize():
        print("Failed to initialize AWS protection")
        return

    if args.enable_advanced:
        print("Enabling AWS Shield Advanced...")
        if aws_protection.enable_shield_advanced():
            print("Shield Advanced enabled successfully")
        else:
            print("Failed to enable Shield Advanced")

    if args.resource_arn:
        print(f"Creating protection for resource: {args.resource_arn}")
        protection_id = aws_protection.create_shield_protection(args.resource_arn, "DDoS-Protection")
        if protection_id:
            print(f"Protection created with ID: {protection_id}")
        else:
            print("Failed to create protection")

    # Create WAF rule
    print("Creating WAF rate limiting rule...")
    rule_id = aws_protection.create_waf_rule("DDoS-Rate-Limit", "Rate limiting for DDoS protection")
    if rule_id:
        print(f"WAF rule created with ID: {rule_id}")
    else:
        print("Failed to create WAF rule")

    print("AWS deployment completed")

if __name__ == "__main__":
    main()

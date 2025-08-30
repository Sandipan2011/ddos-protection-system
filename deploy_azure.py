#!/usr/bin/env python3
"""
Azure Deployment Script for DDoS Protection System
Deploys Azure DDoS Protection for virtual networks
"""

import sys
import os
import argparse

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from cloud_protection.azure_protection import AzureProtection

def main():
    parser = argparse.ArgumentParser(description='Deploy Azure DDoS Protection')
    parser.add_argument('--subscription-id', required=True, help='Azure subscription ID')
    parser.add_argument('--resource-group', required=True, help='Resource group name')
    parser.add_argument('--region', default='East US', help='Azure region')
    parser.add_argument('--vnet-name', help='Virtual network name to protect')
    parser.add_argument('--plan-name', default='DDoS-Protection-Plan', help='DDoS protection plan name')

    args = parser.parse_args()

    azure_protection = AzureProtection(
        subscription_id=args.subscription_id,
        resource_group=args.resource_group,
        region=args.region
    )

    if not azure_protection.initialize():
        print("Failed to initialize Azure protection")
        return

    print(f"Creating DDoS Protection Plan: {args.plan_name}")
    plan_id = azure_protection.create_ddos_protection_plan(args.plan_name)
    if plan_id:
        print(f"Protection plan created: {plan_id}")
    else:
        print("Failed to create protection plan")

    if args.vnet_name:
        print(f"Enabling DDoS protection for VNet: {args.vnet_name}")
        if azure_protection.enable_ddos_protection(args.vnet_name, plan_id):
            print("DDoS protection enabled for VNet")
        else:
            print("Failed to enable DDoS protection")

    print("Azure deployment completed")

if __name__ == "__main__":
    main()

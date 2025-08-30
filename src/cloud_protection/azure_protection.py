#!/usr/bin/env python3
"""
Azure Cloud Protection Module for DDoS Protection System
Integrates with Azure DDoS Protection for virtual networks
"""

import logging
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

class AzureProtection:
    def __init__(self, subscription_id, resource_group, region='East US'):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.region = region
        self.network_client = None
        self.logger = logging.getLogger(__name__)

    def initialize(self):
        try:
            credential = DefaultAzureCredential()
            self.network_client = NetworkManagementClient(credential, self.subscription_id)
            self.logger.info("Azure Network client initialized")
            return True
        except Exception as e:
            self.logger.error(f"Azure initialization failed: {e}")
            return False

    def create_ddos_protection_plan(self, plan_name):
        """Create Azure DDoS Protection Plan"""
        try:
            ddos_plan = self.network_client.ddos_protection_plans.create_or_update(
                resource_group_name=self.resource_group,
                ddos_protection_plan_name=plan_name,
                parameters={
                    'location': self.region,
                    'properties': {}
                }
            )
            self.logger.info(f"DDoS Protection Plan created: {ddos_plan.name}")
            return ddos_plan.name
        except Exception as e:
            self.logger.error(f"Failed to create DDoS Protection Plan: {e}")
            return None

    def enable_ddos_protection(self, vnet_name, ddos_plan_id):
        """Enable DDoS protection for a virtual network"""
        try:
            vnet = self.network_client.virtual_networks.get(
                resource_group_name=self.resource_group,
                virtual_network_name=vnet_name
            )

            vnet.ddos_protection_plan = {
                'id': ddos_plan_id
            }

            updated_vnet = self.network_client.virtual_networks.create_or_update(
                resource_group_name=self.resource_group,
                virtual_network_name=vnet_name,
                parameters=vnet
            )
            self.logger.info(f"DDoS protection enabled for VNet: {vnet_name}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to enable DDoS protection: {e}")
            return False

    def get_ddos_attack_status(self, ddos_plan_name):
        """Get DDoS attack status from protection plan"""
        try:
            ddos_plan = self.network_client.ddos_protection_plans.get(
                resource_group_name=self.resource_group,
                ddos_protection_plan_name=ddos_plan_name
            )
            return ddos_plan.provisioning_state
        except Exception as e:
            self.logger.error(f"Failed to get DDoS status: {e}")
            return None

    def create_nsg_rule(self, nsg_name, rule_name):
        """Create NSG rule for rate limiting"""
        try:
            rule = self.network_client.security_rules.create_or_update(
                resource_group_name=self.resource_group,
                network_security_group_name=nsg_name,
                security_rule_name=rule_name,
                security_rule_parameters={
                    'properties': {
                        'priority': 100,
                        'access': 'Deny',
                        'direction': 'Inbound',
                        'protocol': '*',
                        'sourcePortRange': '*',
                        'destinationPortRange': '*',
                        'sourceAddressPrefix': '*',
                        'destinationAddressPrefix': '*',
                        'description': 'Rate limiting rule for DDoS protection'
                    }
                }
            )
            self.logger.info(f"NSG rule created: {rule.name}")
            return rule.name
        except Exception as e:
            self.logger.error(f"Failed to create NSG rule: {e}")
            return None

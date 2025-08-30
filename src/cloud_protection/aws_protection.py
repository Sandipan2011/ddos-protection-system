#!/usr/bin/env python3
"""
AWS Cloud Protection Module for DDoS Protection System
Integrates with AWS Shield for advanced DDoS protection
"""

import boto3
import logging
from botocore.exceptions import ClientError

class AWSProtection:
    def __init__(self, region='us-east-1'):
        self.region = region
        self.shield_client = None
        self.waf_client = None
        self.logger = logging.getLogger(__name__)

    def initialize(self):
        try:
            self.shield_client = boto3.client('shield', region_name=self.region)
            self.waf_client = boto3.client('wafv2', region_name=self.region)
            self.logger.info("AWS Shield and WAF clients initialized")
            return True
        except Exception as e:
            self.logger.error(f"AWS initialization failed: {e}")
            return False

    def create_shield_protection(self, resource_arn, name):
        """Create AWS Shield protection for a resource"""
        try:
            response = self.shield_client.create_protection(
                Name=name,
                ResourceArn=resource_arn
            )
            self.logger.info(f"Shield protection created: {response['ProtectionId']}")
            return response['ProtectionId']
        except ClientError as e:
            self.logger.error(f"Failed to create Shield protection: {e}")
            return None

    def get_protection_status(self, protection_id):
        """Get the status of a Shield protection"""
        try:
            response = self.shield_client.describe_protection(
                ProtectionId=protection_id
            )
            return response['Protection']
        except ClientError as e:
            self.logger.error(f"Failed to get protection status: {e}")
            return None

    def create_waf_rule(self, name, description, ip_set_arn=None):
        """Create WAF rule for rate limiting"""
        try:
            rule = {
                'Name': name,
                'Priority': 1,
                'Statement': {
                    'RateBasedStatement': {
                        'Limit': 1000,  # requests per 5 minutes
                        'AggregateKeyType': 'IP'
                    }
                },
                'Action': {'Block': {}},
                'VisibilityConfig': {
                    'SampledRequestsEnabled': True,
                    'CloudWatchMetricsEnabled': True,
                    'MetricName': f'{name}Metric'
                }
            }

            if ip_set_arn:
                rule['Statement']['RateBasedStatement']['ScopeDownStatement'] = {
                    'IPSetReferenceStatement': {
                        'ARN': ip_set_arn
                    }
                }

            response = self.waf_client.create_rule(
                Name=name,
                Scope='CLOUDFRONT',  # or REGIONAL
                Description=description,
                Rules=[rule]
            )
            self.logger.info(f"WAF rule created: {response['Summary']['Id']}")
            return response['Summary']['Id']
        except ClientError as e:
            self.logger.error(f"Failed to create WAF rule: {e}")
            return None

    def enable_shield_advanced(self):
        """Enable AWS Shield Advanced subscription"""
        try:
            response = self.shield_client.create_subscription()
            self.logger.info("Shield Advanced subscription enabled")
            return True
        except ClientError as e:
            self.logger.error(f"Failed to enable Shield Advanced: {e}")
            return False

    def get_attack_statistics(self):
        """Get DDoS attack statistics from Shield"""
        try:
            response = self.shield_client.list_attacks(
                MaxResults=10
            )
            return response['AttackSummaries']
        except ClientError as e:
            self.logger.error(f"Failed to get attack statistics: {e}")
            return []

#!/usr/bin/env python3
"""
Cloud Protection Package for DDoS Protection System
"""

from .aws_protection import AWSProtection
from .azure_protection import AzureProtection
from .gcp_protection import GCPProtection

__all__ = ['AWSProtection', 'AzureProtection', 'GCPProtection']

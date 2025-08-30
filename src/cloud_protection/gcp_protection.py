#!/usr/bin/env python3
"""
GCP Cloud Protection Module for DDoS Protection System
Integrates with Google Cloud Armor for load balancers
"""

import logging
from google.cloud import compute_v1
from google.cloud import securitycenter_v1

class GCPProtection:
    def __init__(self, project_id):
        self.project_id = project_id
        self.compute_client = None
        self.security_client = None
        self.logger = logging.getLogger(__name__)

    def initialize(self):
        try:
            self.compute_client = compute_v1.SecurityPoliciesClient()
            self.security_client = securitycenter_v1.SecurityCenterClient()
            self.logger.info("GCP Compute and Security clients initialized")
            return True
        except Exception as e:
            self.logger.error(f"GCP initialization failed: {e}")
            return False

    def create_security_policy(self, policy_name, description="DDoS Protection Policy"):
        """Create Cloud Armor security policy"""
        try:
            policy = compute_v1.SecurityPolicy(
                name=policy_name,
                description=description,
                rules=[
                    compute_v1.SecurityPolicyRule(
                        priority=1000,
                        match=compute_v1.SecurityPolicyRuleMatcher(
                            config=compute_v1.SecurityPolicyRuleMatcherConfig(
                                src_ip_ranges=["*"]
                            ),
                            versioned_expr="SRC_IPS_V1"
                        ),
                        action="deny(403)",
                        description="Block DDoS attacks"
                    ),
                    compute_v1.SecurityPolicyRule(
                        priority=2147483647,
                        match=compute_v1.SecurityPolicyRuleMatcher(
                            config=compute_v1.SecurityPolicyRuleMatcherConfig(
                                src_ip_ranges=["*"]
                            ),
                            versioned_expr="SRC_IPS_V1"
                        ),
                        action="allow",
                        description="Default allow rule"
                    )
                ]
            )

            request = compute_v1.InsertSecurityPolicyRequest(
                project=self.project_id,
                security_policy_resource=policy
            )

            operation = self.compute_client.insert(request)
            self.logger.info(f"Security policy created: {policy_name}")
            return policy_name
        except Exception as e:
            self.logger.error(f"Failed to create security policy: {e}")
            return None

    def attach_policy_to_backend(self, policy_name, backend_service_name, region):
        """Attach security policy to backend service"""
        try:
            backend_service = self.compute_client.get(
                project=self.project_id,
                region=region,
                backend_service=backend_service_name
            )

            backend_service.security_policy = policy_name

            request = compute_v1.UpdateBackendServiceRequest(
                project=self.project_id,
                region=region,
                backend_service=backend_service_name,
                backend_service_resource=backend_service
            )

            operation = self.compute_client.update(request)
            self.logger.info(f"Policy attached to backend service: {backend_service_name}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to attach policy: {e}")
            return False

    def create_rate_limit_rule(self, policy_name, threshold=1000):
        """Create rate limiting rule in security policy"""
        try:
            rule = compute_v1.SecurityPolicyRule(
                priority=500,
                match=compute_v1.SecurityPolicyRuleMatcher(
                    config=compute_v1.SecurityPolicyRuleMatcherConfig(
                        src_ip_ranges=["*"]
                    ),
                    versioned_expr="SRC_IPS_V1"
                ),
                action="rate_based_ban",
                rate_limit_options=compute_v1.SecurityPolicyRuleRateLimitOptions(
                    rate_limit_threshold=compute_v1.SecurityPolicyRuleRateLimitOptionsThreshold(
                        count=threshold,
                        interval_sec=60
                    ),
                    conform_action="allow",
                    exceed_action="deny(429)",
                    ban_duration_sec=300
                ),
                description="Rate limiting for DDoS protection"
            )

            request = compute_v1.AddRuleSecurityPolicyRequest(
                project=self.project_id,
                security_policy=policy_name,
                security_policy_rule_resource=rule
            )

            operation = self.compute_client.add_rule(request)
            self.logger.info(f"Rate limit rule added to policy: {policy_name}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to create rate limit rule: {e}")
            return False

    def get_attack_logs(self):
        """Get security findings related to DDoS attacks"""
        try:
            request = securitycenter_v1.ListFindingsRequest(
                parent=f"projects/{self.project_id}",
                filter='category="DDoS"'
            )

            findings = self.security_client.list_findings(request)
            return [finding for finding in findings]
        except Exception as e:
            self.logger.error(f"Failed to get attack logs: {e}")
            return []

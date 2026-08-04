# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .email_dmarc_policy_param import EmailDmarcPolicyParam
from .domains_tracking_settings_param import DomainsTrackingSettingsParam

__all__ = ["EmailDomainCreateParams"]


class EmailDomainCreateParams(TypedDict, total=False):
    domain: Required[str]

    dmarc_policy: Optional[EmailDmarcPolicyParam]
    """DMARC policy for a sending domain.

    Drives the recommended \\__dmarc.<domain> TXT record. DMARC is advisory and never
    blocks sending. When omitted or null, the domain uses the advisory default
    (v=DMARC1; p=none; rua=mailto:dmarc@telnyx.com).
    """

    inbound_enabled: bool
    """Enable inbound routing for this domain"""

    tracking: DomainsTrackingSettingsParam

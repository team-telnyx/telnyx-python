# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .email_dmarc_policy_param import EmailDmarcPolicyParam
from .domains_tracking_settings_param import DomainsTrackingSettingsParam

__all__ = ["EmailDomainUpdateParams"]


class EmailDomainUpdateParams(TypedDict, total=False):
    dmarc_policy: Optional[EmailDmarcPolicyParam]
    """DMARC policy for a sending domain.

    Drives the recommended \\__dmarc.<domain> TXT record. DMARC is advisory and never
    blocks sending. When omitted or null, the domain uses the advisory default
    (v=DMARC1; p=none; rua=mailto:dmarc@telnyx.com).
    """

    inbound_enabled: bool
    """Enable or disable inbound routing for this domain"""

    tracking: DomainsTrackingSettingsParam

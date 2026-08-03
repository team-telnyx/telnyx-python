# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EmailDmarcPolicyParam"]


class EmailDmarcPolicyParam(TypedDict, total=False):
    """DMARC policy for a sending domain.

    Drives the recommended _dmarc.<domain> TXT record. DMARC is advisory and never blocks sending. When omitted or null, the domain uses the advisory default (v=DMARC1; p=none; rua=mailto:dmarc@telnyx.com).
    """

    p: Literal["none", "quarantine", "reject"]
    """Policy applied to messages that fail alignment."""

    pct: int
    """Percentage of messages the policy applies to. Omitted from the record when 100."""

    rua: Optional[str]
    """URI for aggregate reports.

    Defaults to the Telnyx address when absent; null omits it.
    """

    sp: Optional[Literal["none", "quarantine", "reject"]]
    """Policy for subdomains. Omitted from the record when null."""

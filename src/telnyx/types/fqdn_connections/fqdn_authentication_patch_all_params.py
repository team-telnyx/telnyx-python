# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FqdnAuthenticationPatchAllParams"]


class FqdnAuthenticationPatchAllParams(TypedDict, total=False):
    failover_url: str
    """The failover webhook URL."""

    fqdn_outbound_authentication: Literal["ip-authentication", "credential-authentication"]
    """The outbound authentication type."""

    ip_authentication_method: Literal["token", "p-charge-info"]
    """The IP authentication method."""

    password: str
    """The password for authentication."""

    txt_name: str
    """The TXT record name for Microsoft Teams SBC DNS verification."""

    txt_ttl: int
    """The TTL for the TXT record."""

    txt_value: str
    """The TXT record value for Microsoft Teams SBC DNS verification."""

    user_name: str
    """The username for authentication."""

    webhook_url: str
    """The webhook URL for authentication events."""

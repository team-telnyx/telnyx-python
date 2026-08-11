# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FqdnAuthentication"]


class FqdnAuthentication(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    connection_id: Optional[str] = None
    """The ID of the FQDN connection this authentication strategy belongs to."""

    failover_url: Optional[str] = None
    """The failover webhook URL."""

    fqdn_outbound_authentication: Optional[Literal["ip-authentication", "credential-authentication"]] = None
    """The outbound authentication type."""

    ip_authentication_method: Optional[Literal["token", "p-charge-info"]] = None
    """The IP authentication method."""

    microsoft_teams_sbc: Optional[bool] = None
    """Whether the connection is a Microsoft Teams SBC."""

    password: Optional[str] = None
    """The password for authentication."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    txt_name: Optional[str] = None
    """The TXT record name for Microsoft Teams SBC DNS verification."""

    txt_ttl: Optional[int] = None
    """The TTL for the TXT record."""

    txt_value: Optional[str] = None
    """The TXT record value for Microsoft Teams SBC DNS verification."""

    user_name: Optional[str] = None
    """The username for authentication."""

    webhook_url: Optional[str] = None
    """The webhook URL for authentication events."""

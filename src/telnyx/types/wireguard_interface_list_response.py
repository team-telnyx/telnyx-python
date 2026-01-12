# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .record import Record
from .._models import BaseModel
from .network_interface import NetworkInterface

__all__ = ["WireguardInterfaceListResponse", "WireguardInterfaceListResponseRegion"]


class WireguardInterfaceListResponseRegion(BaseModel):
    code: Optional[str] = None
    """Region code of the interface."""

    name: Optional[str] = None
    """Region name of the interface."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class WireguardInterfaceListResponse(Record, NetworkInterface):
    enable_sip_trunking: Optional[bool] = None
    """Enable SIP traffic forwarding over VPN interface."""

    endpoint: Optional[str] = None
    """The Telnyx WireGuard peers `Peer.endpoint` value."""

    public_key: Optional[str] = None
    """The Telnyx WireGuard peers `Peer.PublicKey`."""

    region: Optional[WireguardInterfaceListResponseRegion] = None

    region_code: Optional[str] = None
    """The region interface is deployed to."""

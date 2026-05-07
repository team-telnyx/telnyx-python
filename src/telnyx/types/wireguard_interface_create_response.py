# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .interface_status import InterfaceStatus

__all__ = ["WireguardInterfaceCreateResponse", "Data", "DataRegion"]


class DataRegion(BaseModel):
    code: Optional[str] = None
    """Region code of the interface."""

    name: Optional[str] = None
    """Region name of the interface."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    enable_sip_trunking: Optional[bool] = None
    """Enable SIP traffic forwarding over VPN interface."""

    endpoint: Optional[str] = None
    """The Telnyx WireGuard peers `Peer.endpoint` value."""

    name: Optional[str] = None
    """A user specified name for the interface."""

    network_id: Optional[str] = None
    """The id of the network associated with the interface."""

    public_key: Optional[str] = None
    """The Telnyx WireGuard peers `Peer.PublicKey`."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    region: Optional[DataRegion] = None

    region_code: Optional[str] = None
    """The region interface is deployed to."""

    status: Optional[InterfaceStatus] = None
    """The current status of the interface deployment."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class WireguardInterfaceCreateResponse(BaseModel):
    data: Optional[Data] = None

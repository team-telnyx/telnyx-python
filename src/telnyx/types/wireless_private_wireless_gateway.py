# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pwg_assigned_resources_summary import PwgAssignedResourcesSummary
from .private_wireless_gateway_status import PrivateWirelessGatewayStatus

__all__ = ["WirelessPrivateWirelessGateway"]


class WirelessPrivateWirelessGateway(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    address_mode: Optional[Literal["static", "dynamic"]] = None
    """The address mode of the private wireless gateway.

    With static, each SIM card gets a fixed IP address from the gateway's IP range
    that is preserved across sessions. With dynamic, IP addresses are assigned by
    the network at attach time and may change between sessions.
    """

    assigned_resources: Optional[List[PwgAssignedResourcesSummary]] = None
    """
    A list of the resources that have been assigned to the Private Wireless Gateway.
    """

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    ip_range: Optional[str] = None
    """IP block used to assign IPs to the SIM cards in the Private Wireless Gateway."""

    name: Optional[str] = None
    """The private wireless gateway name."""

    network_id: Optional[str] = None
    """The identification of the related network resource."""

    record_type: Optional[str] = None

    region_code: Optional[str] = None
    """The name of the region where the Private Wireless Gateway is deployed."""

    status: Optional[PrivateWirelessGatewayStatus] = None
    """The current status or failure details of the Private Wireless Gateway."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""

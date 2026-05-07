# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .interface_status import InterfaceStatus

__all__ = ["VirtualCrossConnectCombined", "Region"]


class Region(BaseModel):
    code: Optional[str] = None
    """Region code of the interface."""

    name: Optional[str] = None
    """Region name of the interface."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class VirtualCrossConnectCombined(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    bandwidth_mbps: Optional[float] = None
    """
    The desired throughput in Megabits per Second (Mbps) for your Virtual Cross
    Connect.
    """

    bgp_asn: Optional[float] = None
    """The Border Gateway Protocol (BGP) Autonomous System Number (ASN)."""

    cloud_provider: Optional[Literal["aws", "azure", "gce"]] = None
    """
    The Virtual Private Cloud with which you would like to establish a cross
    connect.
    """

    cloud_provider_region: Optional[str] = None
    """The region where your Virtual Private Cloud hosts are located."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    name: Optional[str] = None
    """A user specified name for the interface."""

    network_id: Optional[str] = None
    """The id of the network associated with the interface."""

    primary_bgp_key: Optional[str] = None
    """The authentication key for BGP peer configuration."""

    primary_cloud_account_id: Optional[str] = None
    """The identifier for your Virtual Private Cloud."""

    primary_cloud_ip: Optional[str] = None
    """The IP address assigned for your side of the Virtual Cross Connect."""

    primary_enabled: Optional[bool] = None
    """Indicates whether the primary circuit is enabled."""

    primary_routing_announcement: Optional[bool] = None
    """Whether"""

    primary_telnyx_ip: Optional[str] = None
    """The IP address assigned to the Telnyx side of the Virtual Cross Connect."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    region: Optional[Region] = None

    region_code: Optional[str] = None
    """The region interface is deployed to."""

    status: Optional[InterfaceStatus] = None
    """The current status of the interface deployment."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""

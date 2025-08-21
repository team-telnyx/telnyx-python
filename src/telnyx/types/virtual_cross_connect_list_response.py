# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .record import Record
from .._models import BaseModel
from .interface import Interface
from .region_in import RegionIn
from .pagination_meta import PaginationMeta

__all__ = ["VirtualCrossConnectListResponse", "Data", "DataRegion"]


class DataRegion(BaseModel):
    code: Optional[str] = None
    """Region code of the interface."""

    name: Optional[str] = None
    """Region name of the interface."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class Data(Record, Interface, RegionIn):
    bgp_asn: float
    """The Border Gateway Protocol (BGP) Autonomous System Number (ASN).

    If null, value will be assigned by Telnyx.
    """

    cloud_provider: Literal["aws", "azure", "gce"]
    """
    The Virtual Private Cloud with which you would like to establish a cross
    connect.
    """

    cloud_provider_region: str
    """
    The region where your Virtual Private Cloud hosts are located.<br /><br />The
    available regions can be found using the /virtual_cross_connect_regions
    endpoint.
    """

    primary_cloud_account_id: str
    """The identifier for your Virtual Private Cloud.

    The number will be different based upon your Cloud provider.
    """

    region_code: str  # type: ignore
    """The region interface is deployed to."""

    bandwidth_mbps: Optional[float] = None
    """
    The desired throughput in Megabits per Second (Mbps) for your Virtual Cross
    Connect.<br /><br />The available bandwidths can be found using the
    /virtual_cross_connect_regions endpoint.
    """

    primary_bgp_key: Optional[str] = None
    """The authentication key for BGP peer configuration."""

    primary_cloud_ip: Optional[str] = None
    """
    The IP address assigned for your side of the Virtual Cross
    Connect.<br /><br />If none is provided, one will be generated for
    you.<br /><br />This value can not be patched once the VXC has bene provisioned.
    """

    primary_enabled: Optional[bool] = None
    """Indicates whether the primary circuit is enabled.

    Setting this to `false` will disable the circuit.
    """

    primary_routing_announcement: Optional[bool] = None
    """Whether the primary BGP route is being announced."""

    primary_telnyx_ip: Optional[str] = None
    """
    The IP address assigned to the Telnyx side of the Virtual Cross
    Connect.<br /><br />If none is provided, one will be generated for
    you.<br /><br />This value should be null for GCE as Google will only inform you
    of your assigned IP once the connection has been accepted.
    """

    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""

    region: Optional[DataRegion] = None

    secondary_bgp_key: Optional[str] = None
    """The authentication key for BGP peer configuration."""

    secondary_cloud_account_id: Optional[str] = None
    """The identifier for your Virtual Private Cloud.

    The number will be different based upon your Cloud provider.<br /><br />This
    attribute is only necessary for GCE.
    """

    secondary_cloud_ip: Optional[str] = None
    """
    The IP address assigned for your side of the Virtual Cross
    Connect.<br /><br />If none is provided, one will be generated for
    you.<br /><br />This value can not be patched once the VXC has bene provisioned.
    """

    secondary_enabled: Optional[bool] = None
    """Indicates whether the secondary circuit is enabled.

    Setting this to `false` will disable the circuit.
    """

    secondary_routing_announcement: Optional[bool] = None
    """Whether the secondary BGP route is being announced."""

    secondary_telnyx_ip: Optional[str] = None
    """
    The IP address assigned to the Telnyx side of the Virtual Cross
    Connect.<br /><br />If none is provided, one will be generated for
    you.<br /><br />This value should be null for GCE as Google will only inform you
    of your assigned IP once the connection has been accepted.
    """


class VirtualCrossConnectListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

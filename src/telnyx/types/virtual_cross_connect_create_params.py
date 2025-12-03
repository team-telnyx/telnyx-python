# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VirtualCrossConnectCreateParams"]


class VirtualCrossConnectCreateParams(TypedDict, total=False):
    bgp_asn: Required[float]
    """The Border Gateway Protocol (BGP) Autonomous System Number (ASN).

    If null, value will be assigned by Telnyx.
    """

    cloud_provider: Required[Literal["aws", "azure", "gce"]]
    """
    The Virtual Private Cloud with which you would like to establish a cross
    connect.
    """

    cloud_provider_region: Required[str]
    """
    The region where your Virtual Private Cloud hosts are located.<br /><br />The
    available regions can be found using the /virtual_cross_connect_regions
    endpoint.
    """

    network_id: Required[str]
    """The id of the network associated with the interface."""

    primary_cloud_account_id: Required[str]
    """The identifier for your Virtual Private Cloud.

    The number will be different based upon your Cloud provider.
    """

    region_code: Required[str]
    """The region the interface should be deployed to."""

    bandwidth_mbps: float
    """
    The desired throughput in Megabits per Second (Mbps) for your Virtual Cross
    Connect.<br /><br />The available bandwidths can be found using the
    /virtual_cross_connect_regions endpoint.
    """

    name: str
    """A user specified name for the interface."""

    primary_bgp_key: str
    """The authentication key for BGP peer configuration."""

    primary_cloud_ip: str
    """
    The IP address assigned for your side of the Virtual Cross
    Connect.<br /><br />If none is provided, one will be generated for
    you.<br /><br />This value should be null for GCE as Google will only inform you
    of your assigned IP once the connection has been accepted.
    """

    primary_telnyx_ip: str
    """
    The IP address assigned to the Telnyx side of the Virtual Cross
    Connect.<br /><br />If none is provided, one will be generated for
    you.<br /><br />This value should be null for GCE as Google will only inform you
    of your assigned IP once the connection has been accepted.
    """

    secondary_bgp_key: str
    """The authentication key for BGP peer configuration."""

    secondary_cloud_account_id: str
    """The identifier for your Virtual Private Cloud.

    The number will be different based upon your Cloud provider.<br /><br />This
    attribute is only necessary for GCE.
    """

    secondary_cloud_ip: str
    """
    The IP address assigned for your side of the Virtual Cross
    Connect.<br /><br />If none is provided, one will be generated for
    you.<br /><br />This value should be null for GCE as Google will only inform you
    of your assigned IP once the connection has been accepted.
    """

    secondary_telnyx_ip: str
    """
    The IP address assigned to the Telnyx side of the Virtual Cross
    Connect.<br /><br />If none is provided, one will be generated for
    you.<br /><br />This value should be null for GCE as Google will only inform you
    of your assigned IP once the connection has been accepted.
    """

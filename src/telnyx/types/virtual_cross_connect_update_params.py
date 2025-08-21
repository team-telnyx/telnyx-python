# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VirtualCrossConnectUpdateParams"]


class VirtualCrossConnectUpdateParams(TypedDict, total=False):
    primary_cloud_ip: str
    """
    The IP address assigned for your side of the Virtual Cross
    Connect.<br /><br />If none is provided, one will be generated for
    you.<br /><br />This value can not be patched once the VXC has bene provisioned.
    """

    primary_enabled: bool
    """Indicates whether the primary circuit is enabled.

    Setting this to `false` will disable the circuit.
    """

    primary_routing_announcement: bool
    """Whether the primary BGP route is being announced."""

    secondary_cloud_ip: str
    """
    The IP address assigned for your side of the Virtual Cross
    Connect.<br /><br />If none is provided, one will be generated for
    you.<br /><br />This value can not be patched once the VXC has bene provisioned.
    """

    secondary_enabled: bool
    """Indicates whether the secondary circuit is enabled.

    Setting this to `false` will disable the circuit.
    """

    secondary_routing_announcement: bool
    """Whether the secondary BGP route is being announced."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PrivateWirelessGatewayCreateParams"]


class PrivateWirelessGatewayCreateParams(TypedDict, total=False):
    name: Required[str]
    """The private wireless gateway name."""

    network_id: Required[str]
    """The identification of the related network resource."""

    address_mode: Literal["static", "dynamic"]
    """Determines how IP addresses are assigned to SIM cards using this gateway.

    With static, each SIM card gets a fixed IP address from the gateway's IP range
    that is preserved across sessions. With dynamic, an IP address is assigned by
    the network at attach time and may change between sessions. If omitted, the
    gateway is created with the default address mode, dynamic.
    """

    region_code: str
    """The code of the region where the private wireless gateway will be assigned.

    A list of available regions can be found at the regions endpoint
    """

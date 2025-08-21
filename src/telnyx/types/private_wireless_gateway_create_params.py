# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PrivateWirelessGatewayCreateParams"]


class PrivateWirelessGatewayCreateParams(TypedDict, total=False):
    name: Required[str]
    """The private wireless gateway name."""

    network_id: Required[str]
    """The identification of the related network resource."""

    region_code: str
    """The code of the region where the private wireless gateway will be assigned.

    A list of available regions can be found at the regions endpoint
    """

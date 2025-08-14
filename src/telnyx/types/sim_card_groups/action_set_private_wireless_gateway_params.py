# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionSetPrivateWirelessGatewayParams"]


class ActionSetPrivateWirelessGatewayParams(TypedDict, total=False):
    private_wireless_gateway_id: Required[str]
    """The identification of the related Private Wireless Gateway resource."""

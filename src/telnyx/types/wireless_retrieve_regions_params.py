# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WirelessRetrieveRegionsParams"]


class WirelessRetrieveRegionsParams(TypedDict, total=False):
    product: Required[str]
    """
    The product for which to list regions (e.g., 'public_ips',
    'private_wireless_gateways').
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .wireguard_interface_param import WireguardInterfaceParam
from .network_interface_region_param import NetworkInterfaceRegionParam

__all__ = ["WireguardInterfaceCreateParams", "Body"]


class WireguardInterfaceCreateParams(TypedDict, total=False):
    body: Required[Body]


class Body(WireguardInterfaceParam, NetworkInterfaceRegionParam, total=False):
    pass

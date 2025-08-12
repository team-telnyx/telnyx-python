# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WireguardInterfaceCreateParams"]


class WireguardInterfaceCreateParams(TypedDict, total=False):
    network_id: Required[str]
    """The id of the network associated with the interface."""

    region_code: Required[str]
    """The region the interface should be deployed to."""

    enable_sip_trunking: bool
    """Enable SIP traffic forwarding over VPN interface."""

    name: str
    """A user specified name for the interface."""

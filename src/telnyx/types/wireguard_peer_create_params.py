# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WireguardPeerCreateParams"]


class WireguardPeerCreateParams(TypedDict, total=False):
    wireguard_interface_id: Required[str]
    """The id of the wireguard interface associated with the peer."""

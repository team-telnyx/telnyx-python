# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .wireguard_peer_param import WireguardPeerParam

__all__ = ["WireguardPeerCreateParams", "Body"]


class WireguardPeerCreateParams(TypedDict, total=False):
    body: Required[Body]


class Body(WireguardPeerParam, total=False):
    pass

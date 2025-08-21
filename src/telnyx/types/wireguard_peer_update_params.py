# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WireguardPeerUpdateParams"]


class WireguardPeerUpdateParams(TypedDict, total=False):
    public_key: str
    """
    The WireGuard `PublicKey`.<br /><br />If you do not provide a Public Key, a new
    Public and Private key pair will be generated for you.
    """

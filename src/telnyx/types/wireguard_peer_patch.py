# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WireguardPeerPatch"]


class WireguardPeerPatch(BaseModel):
    public_key: Optional[str] = None
    """
    The WireGuard `PublicKey`.<br /><br />If you do not provide a Public Key, a new
    Public and Private key pair will be generated for you.
    """

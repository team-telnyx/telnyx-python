# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .wireguard_peer import WireguardPeer

__all__ = ["WireguardPeerCreateResponse"]


class WireguardPeerCreateResponse(BaseModel):
    data: Optional[WireguardPeer] = None

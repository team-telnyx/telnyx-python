# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .wireguard_peer import WireguardPeer

__all__ = ["WireguardPeerUpdateResponse"]


class WireguardPeerUpdateResponse(BaseModel):
    data: Optional[WireguardPeer] = None

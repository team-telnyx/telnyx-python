# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .tunnel import Tunnel

__all__ = ["TunnelWithToken"]


class TunnelWithToken(Tunnel):
    tunnel_token: Optional[str] = None
    """
    The credential that a tunnel process presents with
    `telnyx-edge tunnel run --token`. Returned only by create and rotate_token.
    Telnyx stores only a hash of it.
    """

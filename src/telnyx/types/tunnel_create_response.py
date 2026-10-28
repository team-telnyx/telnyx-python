# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .tunnel_with_token import TunnelWithToken

__all__ = ["TunnelCreateResponse"]


class TunnelCreateResponse(BaseModel):
    data: Optional[TunnelWithToken] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .tunnel import Tunnel
from .._models import BaseModel

__all__ = ["TunnelRetrieveResponse"]


class TunnelRetrieveResponse(BaseModel):
    data: Optional[Tunnel] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .network_route import NetworkRoute

__all__ = ["NetworkRouteCreateResponse"]


class NetworkRouteCreateResponse(BaseModel):
    data: Optional[NetworkRoute] = None

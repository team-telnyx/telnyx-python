# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .tailscale_subnet_router import TailscaleSubnetRouter

__all__ = ["TailscaleSubnetRouterDeleteResponse"]


class TailscaleSubnetRouterDeleteResponse(BaseModel):
    data: Optional[TailscaleSubnetRouter] = None

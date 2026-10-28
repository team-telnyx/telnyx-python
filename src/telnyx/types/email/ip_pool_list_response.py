# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .ip_pool import IPPool
from ..._models import BaseModel

__all__ = ["IPPoolListResponse"]


class IPPoolListResponse(BaseModel):
    data: List[IPPool]

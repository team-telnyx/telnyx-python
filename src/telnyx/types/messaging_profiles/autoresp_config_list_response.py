# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel
from .auto_resp_config import AutoRespConfig
from ..messaging_pagination_meta_0b38e7044b import MessagingPaginationMeta0b38e7044b

__all__ = ["AutorespConfigListResponse"]


class AutorespConfigListResponse(BaseModel):
    """List of Auto-Response Settings"""

    data: List[AutoRespConfig]

    meta: MessagingPaginationMeta0b38e7044b

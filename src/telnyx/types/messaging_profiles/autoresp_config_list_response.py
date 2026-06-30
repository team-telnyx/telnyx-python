# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List

from ..._models import BaseModel
from .auto_resp_config import AutoRespConfig

if TYPE_CHECKING:
    from ..shared.messaging_pagination_meta import MessagingPaginationMeta

__all__ = ["AutorespConfigListResponse"]


class AutorespConfigListResponse(BaseModel):
    """List of Auto-Response Settings"""

    data: List[AutoRespConfig]

    meta: MessagingPaginationMeta

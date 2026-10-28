# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .tunnel import Tunnel
from .._models import BaseModel
from .netapps_cursor_pagination_meta import NetappsCursorPaginationMeta

__all__ = ["TunnelListResponse"]


class TunnelListResponse(BaseModel):
    data: Optional[List[Tunnel]] = None

    meta: Optional[NetappsCursorPaginationMeta] = None

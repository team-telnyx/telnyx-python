# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .network_route import NetworkRoute
from .netapps_cursor_pagination_meta import NetappsCursorPaginationMeta

__all__ = ["NetworkRouteListResponse"]


class NetworkRouteListResponse(BaseModel):
    data: Optional[List[NetworkRoute]] = None

    meta: Optional[NetappsCursorPaginationMeta] = None

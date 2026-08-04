# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from .._models import BaseModel
from .messaging_pagination_meta_0b38e7044b import MessagingPaginationMeta0b38e7044b

__all__ = ["MessagingProfileMetricListResponse"]


class MessagingProfileMetricListResponse(BaseModel):
    data: Optional[List[Dict[str, object]]] = None

    meta: Optional[MessagingPaginationMeta0b38e7044b] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .shared.messaging_pagination_meta import MessagingPaginationMeta

__all__ = ["MessagingProfileMetricListResponse"]


class MessagingProfileMetricListResponse(BaseModel):
    data: Optional[List[Dict[str, object]]] = None

    meta: Optional[MessagingPaginationMeta] = None

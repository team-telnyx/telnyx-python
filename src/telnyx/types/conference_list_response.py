# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .conference import Conference
from .pagination_meta import PaginationMeta

__all__ = ["ConferenceListResponse"]


class ConferenceListResponse(BaseModel):
    data: Optional[List[Conference]] = None

    meta: Optional[PaginationMeta] = None

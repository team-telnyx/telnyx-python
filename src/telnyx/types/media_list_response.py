# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .media_resource import MediaResource
from .pagination_meta import PaginationMeta

__all__ = ["MediaListResponse"]


class MediaListResponse(BaseModel):
    data: Optional[List[MediaResource]] = None

    meta: Optional[PaginationMeta] = None

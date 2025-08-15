# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .shared.short_code import ShortCode

__all__ = ["ShortCodeListResponse"]


class ShortCodeListResponse(BaseModel):
    data: Optional[List[ShortCode]] = None

    meta: Optional[PaginationMeta] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .access_ip_range import AccessIPRange
from .pagination_meta import PaginationMeta

__all__ = ["AccessIPRangeListResponse"]


class AccessIPRangeListResponse(BaseModel):
    data: List[AccessIPRange]

    meta: PaginationMeta

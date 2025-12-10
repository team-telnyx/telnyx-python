# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .fax_application import FaxApplication
from .pagination_meta import PaginationMeta

__all__ = ["FaxApplicationListResponse"]


class FaxApplicationListResponse(BaseModel):
    data: Optional[List[FaxApplication]] = None

    meta: Optional[PaginationMeta] = None

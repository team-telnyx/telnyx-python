# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .dir.dir import Dir
from .._models import BaseModel
from .branded_calling_pagination_meta import BrandedCallingPaginationMeta

__all__ = ["DirList"]


class DirList(BaseModel):
    data: List[Dir]

    meta: BrandedCallingPaginationMeta
    """JSON:API pagination metadata returned with every paginated list response.

    Page numbering is 1-based. `page_size` reports the number of items actually
    returned in `data` for this page; the requested size is taken from the
    `page[size]` query parameter.
    """

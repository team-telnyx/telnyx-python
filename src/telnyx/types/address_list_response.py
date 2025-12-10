# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .address import Address
from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["AddressListResponse"]


class AddressListResponse(BaseModel):
    data: Optional[List[Address]] = None

    meta: Optional[PaginationMeta] = None

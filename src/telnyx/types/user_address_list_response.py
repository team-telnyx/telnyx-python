# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .user_address import UserAddress
from .pagination_meta import PaginationMeta

__all__ = ["UserAddressListResponse"]


class UserAddressListResponse(BaseModel):
    data: Optional[List[UserAddress]] = None

    meta: Optional[PaginationMeta] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .number_order_phone_number import NumberOrderPhoneNumber

__all__ = ["NumberOrderPhoneNumberListResponse"]


class NumberOrderPhoneNumberListResponse(BaseModel):
    data: Optional[List[NumberOrderPhoneNumber]] = None

    meta: Optional[PaginationMeta] = None

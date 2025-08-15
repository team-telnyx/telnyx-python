# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .phone_number_detailed import PhoneNumberDetailed

__all__ = ["PhoneNumberListResponse"]


class PhoneNumberListResponse(BaseModel):
    data: Optional[List[PhoneNumberDetailed]] = None

    meta: Optional[PaginationMeta] = None

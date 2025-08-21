# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..verification import Verification

__all__ = ["ByPhoneNumberListResponse", "Meta"]


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class ByPhoneNumberListResponse(BaseModel):
    data: List[Verification]

    meta: Meta

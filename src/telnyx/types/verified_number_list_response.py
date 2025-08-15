# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .verified_number import VerifiedNumber

__all__ = ["VerifiedNumberListResponse", "Meta"]


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class VerifiedNumberListResponse(BaseModel):
    data: List[VerifiedNumber]

    meta: Meta

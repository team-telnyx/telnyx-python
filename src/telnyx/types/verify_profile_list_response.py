# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .verify_profile import VerifyProfile

__all__ = ["VerifyProfileListResponse", "Meta"]


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class VerifyProfileListResponse(BaseModel):
    data: List[VerifyProfile]

    meta: Meta

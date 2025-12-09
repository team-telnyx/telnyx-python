# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.short_code import ShortCode

__all__ = ["MessagingProfileListShortCodesResponse", "Meta"]


class Meta(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int


class MessagingProfileListShortCodesResponse(BaseModel):
    data: Optional[List[ShortCode]] = None

    meta: Optional[Meta] = None

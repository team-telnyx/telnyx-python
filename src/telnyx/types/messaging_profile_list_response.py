# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .messaging_profile import MessagingProfile

__all__ = ["MessagingProfileListResponse", "Meta"]


class Meta(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int


class MessagingProfileListResponse(BaseModel):
    data: Optional[List[MessagingProfile]] = None

    meta: Optional[Meta] = None

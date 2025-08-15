# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .texml_application import TexmlApplication

__all__ = ["TexmlApplicationListResponse", "Meta"]


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class TexmlApplicationListResponse(BaseModel):
    data: Optional[List[TexmlApplication]] = None

    meta: Optional[Meta] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .spend_limit import SpendLimit

__all__ = ["SpendLimitListResponse", "Meta"]


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class SpendLimitListResponse(BaseModel):
    data: List[SpendLimit]

    meta: Optional[Meta] = None

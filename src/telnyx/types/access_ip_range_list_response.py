# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .access_ip_range import AccessIPRange

__all__ = ["AccessIPRangeListResponse", "Meta"]


class Meta(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int


class AccessIPRangeListResponse(BaseModel):
    data: List[AccessIPRange]

    meta: Meta

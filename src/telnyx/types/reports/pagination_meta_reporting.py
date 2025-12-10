# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PaginationMetaReporting"]


class PaginationMetaReporting(BaseModel):
    page_number: int

    total_pages: int

    page_size: Optional[int] = None

    total_results: Optional[int] = None

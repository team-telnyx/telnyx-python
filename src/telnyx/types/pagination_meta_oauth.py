# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PaginationMetaOAuth"]


class PaginationMetaOAuth(BaseModel):
    page_number: int
    """Current page number"""

    total_pages: int
    """Total number of pages"""

    page_size: Optional[int] = None
    """Number of items per page"""

    total_results: Optional[int] = None
    """Total number of results"""

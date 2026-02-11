# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Metadata"]


class Metadata(BaseModel):
    page_number: int
    """Current Page based on pagination settings (included when defaults are used.)"""

    total_pages: int
    """Total number of pages based on pagination settings"""

    page_size: Optional[int] = None
    """
    Number of results to return per page based on pagination settings (included when
    defaults are used.)
    """

    total_results: Optional[int] = None
    """Total number of results"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Metadata"]


class Metadata(BaseModel):
    page_number: Optional[float] = None
    """Current Page based on pagination settings (included when defaults are used.)"""

    page_size: Optional[float] = None
    """
    Number of results to return per page based on pagination settings (included when
    defaults are used.)
    """

    total_pages: Optional[float] = None
    """Total number of pages based on pagination settings"""

    total_results: Optional[float] = None
    """Total number of results"""

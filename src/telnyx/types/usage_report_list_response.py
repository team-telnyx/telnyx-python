# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["UsageReportListResponse", "Meta"]


class Meta(BaseModel):
    page_number: Optional[int] = None
    """Selected page number."""

    page_size: Optional[int] = None
    """Records per single page"""

    total_pages: Optional[int] = None
    """Total number of pages."""

    total_results: Optional[int] = None
    """Total number of results."""


class UsageReportListResponse(BaseModel):
    data: Optional[List[Dict[str, object]]] = None

    meta: Optional[Meta] = None

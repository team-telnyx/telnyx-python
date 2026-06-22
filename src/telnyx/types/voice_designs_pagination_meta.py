# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VoiceDesignsPaginationMeta"]


class VoiceDesignsPaginationMeta(BaseModel):
    """Pagination metadata returned with list responses."""

    page_number: Optional[int] = None
    """Current page number (1-based)."""

    page_size: Optional[int] = None
    """Number of results per page."""

    total_pages: Optional[int] = None
    """Total number of pages."""

    total_results: Optional[int] = None
    """Total number of results across all pages."""

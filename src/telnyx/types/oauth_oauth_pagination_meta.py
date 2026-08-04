# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["OAuthOAuthPaginationMeta"]


class OAuthOAuthPaginationMeta(BaseModel):
    page_number: Optional[int] = None
    """Current page number"""

    page_size: Optional[int] = None
    """Number of items per page"""

    total_pages: Optional[int] = None
    """Total number of pages"""

    total_results: Optional[int] = None
    """Total number of results"""

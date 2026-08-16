# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WebSearchResult"]


class WebSearchResult(BaseModel):
    description: str
    """Short description or excerpt."""

    snippets: List[str]
    """Relevant text snippets from the page."""

    title: str
    """Result title."""

    url: str
    """Result URL."""

    favicon_url: Optional[str] = None
    """Favicon URL (if available)."""

    thumbnail_url: Optional[str] = None
    """Thumbnail image URL (if available)."""

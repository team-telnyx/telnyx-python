# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._models import BaseModel

__all__ = ["PageMeta"]


class PageMeta(BaseModel):
    page_number: int
    """The page returned, counting from 1."""

    page_size: int
    """Results per page."""

    total_pages: int
    """Pages that can be requested; 0 when nothing matched."""

    total_results: int
    """Results across every page."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProductListParams"]


class ProductListParams(TypedDict, total=False):
    page_number: int
    """Page number (1-based)."""

    page_size: int
    """Number of items per page (max 100)."""

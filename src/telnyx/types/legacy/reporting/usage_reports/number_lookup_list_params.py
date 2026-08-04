# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NumberLookupListParams"]


class NumberLookupListParams(TypedDict, total=False):
    page: int
    """Page number to retrieve (1-based)."""

    per_page: int
    """Filter results by per page."""

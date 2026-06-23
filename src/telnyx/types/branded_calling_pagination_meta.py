# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BrandedCallingPaginationMeta"]


class BrandedCallingPaginationMeta(BaseModel):
    """JSON:API pagination metadata returned with every paginated list response.

    Page numbering is 1-based. `page_size` reports the number of items actually returned in `data` for this page; the requested size is taken from the `page[size]` query parameter.
    """

    page_number: int
    """1-based index of this page.

    Echoes the `page[number]` query parameter (default `1`).
    """

    page_size: int
    """Number of items returned in this page's `data` array. Capped at 250."""

    total_pages: int
    """Total number of pages available given the current `page_size`."""

    total_results: int
    """Total number of items across all pages (excludes soft-deleted rows)."""

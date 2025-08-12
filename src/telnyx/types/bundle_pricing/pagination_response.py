# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PaginationResponse"]


class PaginationResponse(BaseModel):
    page_number: int
    """The current page number."""

    page_size: int
    """The number of results per page."""

    total_pages: int
    """Total number of pages from the results."""

    total_results: int
    """Total number of results returned."""

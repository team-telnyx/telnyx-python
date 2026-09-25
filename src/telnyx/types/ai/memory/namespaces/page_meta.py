# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._models import BaseModel

__all__ = ["PageMeta"]


class PageMeta(BaseModel):
    """Where a listing's page sits in the whole.

    A page is a snapshot: the counts it reports and the order it is drawn in
    both move as writes land, so paging through a busy namespace can repeat or
    miss an entry at a page boundary.
    """

    page_number: int
    """The page returned, counting from 1."""

    page_size: int
    """How many results a page holds."""

    total_pages: int
    """Pages that can be requested; 0 when nothing matched.

    Page until `page_number` reaches it rather than until a page comes back short: a
    page can hold fewer than `page_size` results without being the last. Capped at
    the deepest page served, so on a very large listing it covers fewer results than
    `total_results`.
    """

    total_results: int
    """Results the request matched, including any past the deepest page."""

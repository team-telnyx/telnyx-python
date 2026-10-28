# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["NetappsCursorPaginationMeta", "Cursors"]


class Cursors(BaseModel):
    """Opaque cursors. Absent keys mean there is no such page."""

    after: Optional[str] = None
    """Pass as `page[after]` to fetch the next page. Absent on the last page."""

    before: Optional[str] = None
    """The cursor of the previous page. Present when the request used `page[after]`."""


class NetappsCursorPaginationMeta(BaseModel):
    cursors: Optional[Cursors] = None
    """Opaque cursors. Absent keys mean there is no such page."""

    next: Optional[str] = None
    """The path of the next page, with the same query parameters.

    Absent on the last page.
    """

    previous: Optional[str] = None
    """The path of the previous page. Present when the request used `page[after]`."""

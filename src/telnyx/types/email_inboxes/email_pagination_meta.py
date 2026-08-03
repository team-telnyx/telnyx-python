# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["EmailPaginationMeta"]


class EmailPaginationMeta(BaseModel):
    page_size: int

    page_cursor: Optional[str] = None
    """Cursor for the next page, when more results are available."""

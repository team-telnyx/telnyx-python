# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["KeyListResponse", "Data", "Meta"]


class Data(BaseModel):
    key: Optional[str] = None

    size_bytes: Optional[int] = None
    """Size of the stored value in bytes."""

    updated_at: Optional[datetime] = None


class Meta(BaseModel):
    cursor: Optional[str] = None
    """Opaque cursor for the next page; pass it back as the `cursor` query parameter.

    Omitted when there are no further results.
    """

    has_more: Optional[bool] = None
    """Whether more results are available on a following page."""


class KeyListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None

    record_type: Optional[str] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["KeyListResponse"]


class KeyListResponse(BaseModel):
    key: Optional[str] = None

    size_bytes: Optional[int] = None
    """Size of the stored value in bytes."""

    updated_at: Optional[datetime] = None

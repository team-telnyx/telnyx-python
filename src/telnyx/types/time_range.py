# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TimeRange"]


class TimeRange(BaseModel):
    from_: Optional[datetime] = FieldInfo(alias="from", default=None)

    to: Optional[datetime] = None

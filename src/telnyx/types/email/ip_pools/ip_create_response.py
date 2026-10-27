# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["IPCreateResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[datetime] = None

    dedicated_ip_id: Optional[str] = None

    pool_id: Optional[str] = None

    weight: Optional[int] = None


class IPCreateResponse(BaseModel):
    data: Data

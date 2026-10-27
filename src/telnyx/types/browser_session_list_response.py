# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .session import Session
from .._models import BaseModel

__all__ = ["BrowserSessionListResponse"]


class BrowserSessionListResponse(BaseModel):
    data: Optional[List[Session]] = None

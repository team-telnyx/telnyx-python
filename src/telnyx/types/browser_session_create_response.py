# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .session import Session
from .._models import BaseModel

__all__ = ["BrowserSessionCreateResponse"]


class BrowserSessionCreateResponse(BaseModel):
    data: Optional[Session] = None

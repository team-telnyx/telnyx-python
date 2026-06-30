# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .connection import Connection

__all__ = ["ConnectionRetrieveResponse"]


class ConnectionRetrieveResponse(BaseModel):
    data: Optional[Connection] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .connection import Connection

__all__ = ["ConnectionRetrieveResponse"]


class ConnectionRetrieveResponse(BaseModel):
    data: Optional[Connection] = None

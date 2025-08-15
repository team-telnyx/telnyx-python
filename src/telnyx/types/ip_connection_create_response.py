# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .ip_connection import IPConnection

__all__ = ["IPConnectionCreateResponse"]


class IPConnectionCreateResponse(BaseModel):
    data: Optional[IPConnection] = None

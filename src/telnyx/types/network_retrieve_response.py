# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .network import Network
from .._models import BaseModel

__all__ = ["NetworkRetrieveResponse"]


class NetworkRetrieveResponse(BaseModel):
    data: Optional[Network] = None

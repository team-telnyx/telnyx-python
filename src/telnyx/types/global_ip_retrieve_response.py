# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .global_ip import GlobalIP

__all__ = ["GlobalIPRetrieveResponse"]


class GlobalIPRetrieveResponse(BaseModel):
    data: Optional[GlobalIP] = None

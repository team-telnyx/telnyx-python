# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .global_ip import GlobalIP

__all__ = ["GlobalIPCreateResponse"]


class GlobalIPCreateResponse(BaseModel):
    data: Optional[GlobalIP] = None

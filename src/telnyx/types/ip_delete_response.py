# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .ip import IP
from .._models import BaseModel

__all__ = ["IPDeleteResponse"]


class IPDeleteResponse(BaseModel):
    data: Optional[IP] = None

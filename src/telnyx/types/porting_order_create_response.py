# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .porting_order import PortingOrder

__all__ = ["PortingOrderCreateResponse"]


class PortingOrderCreateResponse(BaseModel):
    data: Optional[List[PortingOrder]] = None

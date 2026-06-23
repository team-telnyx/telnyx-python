# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .advanced_order import AdvancedOrder

__all__ = ["AdvancedOrderListResponse"]


class AdvancedOrderListResponse(BaseModel):
    data: Optional[List[AdvancedOrder]] = None

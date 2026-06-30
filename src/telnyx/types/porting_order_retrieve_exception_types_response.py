# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .shared.porting_orders_exception_type import PortingOrdersExceptionType

__all__ = ["PortingOrderRetrieveExceptionTypesResponse"]


class PortingOrderRetrieveExceptionTypesResponse(BaseModel):
    data: Optional[List[PortingOrdersExceptionType]] = None

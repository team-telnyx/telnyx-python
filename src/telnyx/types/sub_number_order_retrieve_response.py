# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .sub_number_order import SubNumberOrder

__all__ = ["SubNumberOrderRetrieveResponse"]


class SubNumberOrderRetrieveResponse(BaseModel):
    data: Optional[SubNumberOrder] = None

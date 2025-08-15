# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .number_block_order import NumberBlockOrder

__all__ = ["NumberBlockOrderRetrieveResponse"]


class NumberBlockOrderRetrieveResponse(BaseModel):
    data: Optional[NumberBlockOrder] = None

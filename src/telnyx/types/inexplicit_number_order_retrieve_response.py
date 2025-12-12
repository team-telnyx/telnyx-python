# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .inexplicit_number_order_response import InexplicitNumberOrderResponse

__all__ = ["InexplicitNumberOrderRetrieveResponse"]


class InexplicitNumberOrderRetrieveResponse(BaseModel):
    data: Optional[InexplicitNumberOrderResponse] = None

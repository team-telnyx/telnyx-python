# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .number_order_with_phone_numbers import NumberOrderWithPhoneNumbers

__all__ = ["NumberOrderRetrieveResponse"]


class NumberOrderRetrieveResponse(BaseModel):
    data: Optional[NumberOrderWithPhoneNumbers] = None

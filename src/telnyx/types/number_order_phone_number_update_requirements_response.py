# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .number_order_phone_number import NumberOrderPhoneNumber

__all__ = ["NumberOrderPhoneNumberUpdateRequirementsResponse"]


class NumberOrderPhoneNumberUpdateRequirementsResponse(BaseModel):
    data: Optional[NumberOrderPhoneNumber] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .numbers_phone_number_detailed import NumbersPhoneNumberDetailed

__all__ = ["PhoneNumberUpdateResponse"]


class PhoneNumberUpdateResponse(BaseModel):
    data: Optional[NumbersPhoneNumberDetailed] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .porting_phone_number_block import PortingPhoneNumberBlock

__all__ = ["PhoneNumberBlockCreateResponse"]


class PhoneNumberBlockCreateResponse(BaseModel):
    data: Optional[PortingPhoneNumberBlock] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .mobile_phone_number import MobilePhoneNumber

__all__ = ["MobilePhoneNumberUpdateResponse"]


class MobilePhoneNumberUpdateResponse(BaseModel):
    data: Optional[MobilePhoneNumber] = None

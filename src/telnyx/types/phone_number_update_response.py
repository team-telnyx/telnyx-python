# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .phone_number_detailed import PhoneNumberDetailed

__all__ = ["PhoneNumberUpdateResponse"]


class PhoneNumberUpdateResponse(BaseModel):
    data: Optional[PhoneNumberDetailed] = None

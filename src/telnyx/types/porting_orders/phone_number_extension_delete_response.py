# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .porting_phone_number_extension import PortingPhoneNumberExtension

__all__ = ["PhoneNumberExtensionDeleteResponse"]


class PhoneNumberExtensionDeleteResponse(BaseModel):
    data: Optional[PortingPhoneNumberExtension] = None

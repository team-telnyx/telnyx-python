# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .porting_phone_number_configuration import PortingPhoneNumberConfiguration

__all__ = ["PhoneNumberConfigurationCreateResponse"]


class PhoneNumberConfigurationCreateResponse(BaseModel):
    data: Optional[List[PortingPhoneNumberConfiguration]] = None

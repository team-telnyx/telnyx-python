# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .external_connection_phone_number import ExternalConnectionPhoneNumber

__all__ = ["PhoneNumberRetrieveResponse"]


class PhoneNumberRetrieveResponse(BaseModel):
    data: Optional[ExternalConnectionPhoneNumber] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .whatsapp_phone_response import WhatsappPhoneResponse

__all__ = ["PhoneNumberRetrievePhoneNumberResponse"]


class PhoneNumberRetrievePhoneNumberResponse(BaseModel):
    data: WhatsappPhoneResponse

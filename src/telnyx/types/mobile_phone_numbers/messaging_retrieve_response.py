# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .mobile_phone_number_with_messaging_settings import MobilePhoneNumberWithMessagingSettings

__all__ = ["MessagingRetrieveResponse"]


class MessagingRetrieveResponse(BaseModel):
    data: Optional[MobilePhoneNumberWithMessagingSettings] = None

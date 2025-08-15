# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.phone_number_with_messaging_settings import PhoneNumberWithMessagingSettings

__all__ = ["MessagingRetrieveResponse"]


class MessagingRetrieveResponse(BaseModel):
    data: Optional[PhoneNumberWithMessagingSettings] = None

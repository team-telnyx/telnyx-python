# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..shared.phone_number_with_messaging_settings import PhoneNumberWithMessagingSettings

__all__ = ["MessagingRetrieveResponse"]


class MessagingRetrieveResponse(BaseModel):
    data: Optional[PhoneNumberWithMessagingSettings] = None

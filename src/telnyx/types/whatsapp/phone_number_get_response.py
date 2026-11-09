# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .whatsapp_phone_response import WhatsappPhoneResponse
from ..shared.messaging_pagination_meta import MessagingPaginationMeta

__all__ = ["PhoneNumberGetResponse"]


class PhoneNumberGetResponse(BaseModel):
    data: Optional[List[WhatsappPhoneResponse]] = None

    meta: Optional[MessagingPaginationMeta] = None

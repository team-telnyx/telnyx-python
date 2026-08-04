# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..shared.messaging_pagination_meta import MessagingPaginationMeta

__all__ = ["PhoneNumberGetResponse", "Data"]


class Data(BaseModel):
    calling_enabled: Optional[bool] = None

    created_at: Optional[datetime] = None

    display_name: Optional[str] = None

    enabled: Optional[bool] = None

    phone_number: Optional[str] = None
    """Phone number in E164 format"""

    phone_number_id: Optional[str] = None
    """Whatsapp phone number ID"""

    quality_rating: Optional[str] = None
    """Whatsapp quality rating"""

    record_type: Optional[str] = None

    status: Optional[str] = None

    user_id: Optional[str] = None
    """User ID"""

    waba_id: Optional[str] = None
    """WABA ID of Whatsapp business account"""


class PhoneNumberGetResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[MessagingPaginationMeta] = None

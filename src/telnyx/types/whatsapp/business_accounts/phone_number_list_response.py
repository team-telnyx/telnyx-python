# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["PhoneNumberListResponse"]


class PhoneNumberListResponse(BaseModel):
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

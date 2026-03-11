# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ProfileUpdateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    about: Optional[str] = None

    address: Optional[str] = None

    category: Optional[str] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    display_name: Optional[str] = None

    email: Optional[str] = None

    phone_number_id: Optional[str] = None
    """Whatsapp phone number ID"""

    profile_photo_url: Optional[str] = None

    record_type: Optional[str] = None

    updated_at: Optional[datetime] = None

    website: Optional[str] = None


class ProfileUpdateResponse(BaseModel):
    data: Optional[Data] = None

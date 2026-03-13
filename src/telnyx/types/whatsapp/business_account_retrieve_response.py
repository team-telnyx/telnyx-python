# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["BusinessAccountRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Internal ID of Whatsapp business account"""

    account_review_status: Optional[str] = None
    """Account review status of Whatsapp business account"""

    business_verification_status: Optional[str] = None
    """Business verification status of Whatsapp business account"""

    country: Optional[str] = None
    """Country associated with Whatsapp business account"""

    created_at: Optional[datetime] = None

    name: Optional[str] = None
    """Name of Whatsapp business account"""

    phone_numbers_count: Optional[int] = None
    """Count of phone numbers associated with Whatsapp business account"""

    record_type: Optional[str] = None

    status: Optional[str] = None
    """Status of Whatsapp business account"""

    waba_id: Optional[str] = None
    """WABA ID of Whatsapp business account"""


class BusinessAccountRetrieveResponse(BaseModel):
    data: Optional[Data] = None

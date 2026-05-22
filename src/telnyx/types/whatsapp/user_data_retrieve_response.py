# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["UserDataRetrieveResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[datetime] = None

    record_type: Optional[str] = None

    updated_at: Optional[datetime] = None

    webhook_failover_url: Optional[str] = None
    """Failover URL to receive Whatsapp signup events"""

    webhook_url: Optional[str] = None
    """URL to receive Whatsapp signup events"""


class UserDataRetrieveResponse(BaseModel):
    data: Optional[Data] = None

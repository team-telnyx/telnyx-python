# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["SettingUpdateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Internal ID of Whatsapp business account"""

    name: Optional[str] = None

    record_type: Optional[str] = None

    timezone: Optional[str] = None

    updated_at: Optional[datetime] = None

    webhook_enabled: Optional[bool] = None
    """Enable/disable receiving Whatsapp events"""

    webhook_events: Optional[List[str]] = None

    webhook_failover_url: Optional[str] = None
    """Failover URL to receive Whatsapp events"""

    webhook_url: Optional[str] = None
    """URL to receive Whatsapp events"""


class SettingUpdateResponse(BaseModel):
    data: Optional[Data] = None

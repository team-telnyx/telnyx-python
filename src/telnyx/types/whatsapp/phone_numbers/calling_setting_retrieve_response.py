# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["CallingSettingRetrieveResponse", "Data"]


class Data(BaseModel):
    enabled: Optional[bool] = None
    """True if calling is enabled on the phone"""

    phone_number: Optional[str] = None
    """Phone number in E164 format"""

    record_type: Optional[str] = None

    updated_at: Optional[datetime] = None


class CallingSettingRetrieveResponse(BaseModel):
    data: Optional[Data] = None

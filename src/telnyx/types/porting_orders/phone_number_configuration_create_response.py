# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["PhoneNumberConfigurationCreateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies this phone number configuration"""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    porting_phone_number_id: Optional[str] = None
    """Identifies the associated porting phone number"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

    user_bundle_id: Optional[str] = None
    """Identifies the associated user bundle"""


class PhoneNumberConfigurationCreateResponse(BaseModel):
    data: Optional[List[Data]] = None

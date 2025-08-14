# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["VerificationCodeVerifyResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies this porting verification code"""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    phone_number: Optional[str] = None
    """E164 formatted phone number"""

    porting_order_id: Optional[str] = None
    """Identifies the associated porting order"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

    verified: Optional[bool] = None
    """Indicates whether the verification code has been verified"""


class VerificationCodeVerifyResponse(BaseModel):
    data: Optional[List[Data]] = None

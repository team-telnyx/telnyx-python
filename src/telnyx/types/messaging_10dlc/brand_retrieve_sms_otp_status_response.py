# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BrandRetrieveSMSOtpStatusResponse"]


class BrandRetrieveSMSOtpStatusResponse(BaseModel):
    """
    Status information for an SMS OTP sent during Sole Proprietor brand verification
    """

    brand_id: str = FieldInfo(alias="brandId")
    """The Brand ID associated with this OTP request"""

    delivery_status: str = FieldInfo(alias="deliveryStatus")
    """The current delivery status of the OTP SMS message.

    Common values include: `DELIVERED_HANDSET`, `PENDING`, `FAILED`, `EXPIRED`
    """

    mobile_phone: str = FieldInfo(alias="mobilePhone")
    """The mobile phone number where the OTP was sent, in E.164 format"""

    reference_id: str = FieldInfo(alias="referenceId")
    """The reference ID for this OTP request, used for status queries"""

    request_date: datetime = FieldInfo(alias="requestDate")
    """The timestamp when the OTP request was initiated"""

    delivery_status_date: Optional[datetime] = FieldInfo(alias="deliveryStatusDate", default=None)
    """The timestamp when the delivery status was last updated"""

    delivery_status_details: Optional[str] = FieldInfo(alias="deliveryStatusDetails", default=None)
    """Additional details about the delivery status"""

    verify_date: Optional[datetime] = FieldInfo(alias="verifyDate", default=None)
    """The timestamp when the OTP was successfully verified (if applicable)"""

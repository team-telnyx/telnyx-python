# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .rcs_to_item import RcsToItem
from .whatsapp_message_content import WhatsappMessageContent

__all__ = ["MessageSendWhatsappResponse", "Data", "DataFrom"]


class DataFrom(BaseModel):
    carrier: Optional[str] = None
    """The carrier of the sender."""

    line_type: Optional[Literal["Wireline", "Wireless", "VoWiFi", "VoIP", "Pre-Paid Wireless", ""]] = None
    """The line-type of the sender."""

    phone_number: Optional[str] = None
    """
    Sending address (+E.164 formatted phone number, alphanumeric sender ID, or short
    code).
    """

    status: Optional[Literal["received", "delivered"]] = None


class Data(BaseModel):
    id: Optional[str] = None
    """message ID"""

    body: Optional[WhatsappMessageContent] = None

    direction: Optional[str] = None

    encoding: Optional[str] = None

    from_: Optional[DataFrom] = FieldInfo(alias="from", default=None)

    messaging_profile_id: Optional[str] = None

    organization_id: Optional[str] = None

    received_at: Optional[datetime] = None

    record_type: Optional[str] = None

    to: Optional[List[RcsToItem]] = None

    type: Optional[str] = None

    wait_seconds: Optional[float] = None
    """
    Seconds the message is queued due to rate limiting before being sent to the
    carrier. Represents the maximum wait across all applicable rate limits (account,
    carrier, campaign). 0.0 = no queuing delay.
    """


class MessageSendWhatsappResponse(BaseModel):
    data: Optional[Data] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ReplacedLinkClickWebhookEvent", "Data"]


class Data(BaseModel):
    message_id: Optional[str] = None
    """The message ID associated with the clicked link."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    time_clicked: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the message request was received."""

    to: Optional[str] = None
    """
    Sending address (+E.164 formatted phone number, alphanumeric sender ID, or short
    code).
    """

    url: Optional[str] = None
    """The original link that was sent in the message."""


class ReplacedLinkClickWebhookEvent(BaseModel):
    data: Optional[Data] = None

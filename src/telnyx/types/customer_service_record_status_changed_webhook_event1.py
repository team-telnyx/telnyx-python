# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CustomerServiceRecordStatusChangedWebhookEvent", "Data", "DataPayload", "Meta"]


class DataPayload(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the customer service record."""

    phone_number: Optional[str] = None
    """The phone number of the customer service record."""

    status: Optional[Literal["pending", "completed", "failed"]] = None
    """The status of the customer service record"""

    updated_at: Optional[datetime] = None
    """
    ISO 8601 formatted date indicating the last time where the resource was updated.
    """


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the callback event."""

    event_type: Optional[Literal["customer_service_record.status_changed"]] = None
    """The type of the callback event."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the callback event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class Meta(BaseModel):
    attempt: Optional[int] = None
    """The number of times the callback webhook has been attempted."""

    delivered_to: Optional[str] = None
    """The URL that the callback webhook was delivered to."""


class CustomerServiceRecordStatusChangedWebhookEvent(BaseModel):
    data: Optional[Data] = None

    meta: Optional[Meta] = None

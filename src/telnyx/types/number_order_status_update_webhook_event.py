# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .number_order_with_phone_numbers import NumberOrderWithPhoneNumbers

__all__ = ["NumberOrderStatusUpdateWebhookEvent", "Data", "Meta"]


class Data(BaseModel):
    id: str
    """Unique identifier for the event"""

    event_type: str
    """The type of event being sent"""

    occurred_at: datetime
    """ISO 8601 timestamp of when the event occurred"""

    payload: NumberOrderWithPhoneNumbers

    record_type: str
    """Type of record"""


class Meta(BaseModel):
    attempt: int
    """Webhook delivery attempt number"""

    delivered_to: str
    """URL where the webhook was delivered"""


class NumberOrderStatusUpdateWebhookEvent(BaseModel):
    data: Data

    meta: Meta

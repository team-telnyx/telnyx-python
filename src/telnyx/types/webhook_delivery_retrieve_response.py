# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "WebhookDeliveryRetrieveResponse",
    "Data",
    "DataAttempt",
    "DataAttemptHTTP",
    "DataAttemptHTTPRequest",
    "DataAttemptHTTPResponse",
    "DataWebhook",
]


class DataAttemptHTTPRequest(BaseModel):
    """Request details."""

    headers: Optional[List[List[str]]] = None
    """List of headers, limited to 10kB."""

    url: Optional[str] = None


class DataAttemptHTTPResponse(BaseModel):
    """Response details, optional."""

    body: Optional[str] = None
    """Raw response body, limited to 10kB."""

    headers: Optional[List[List[str]]] = None
    """List of headers, limited to 10kB."""

    status: Optional[int] = None


class DataAttemptHTTP(BaseModel):
    """HTTP request and response information."""

    request: Optional[DataAttemptHTTPRequest] = None
    """Request details."""

    response: Optional[DataAttemptHTTPResponse] = None
    """Response details, optional."""


class DataAttempt(BaseModel):
    """Webhook delivery attempt details."""

    errors: Optional[List[int]] = None
    """Webhook delivery error codes."""

    finished_at: Optional[datetime] = None
    """ISO 8601 timestamp indicating when the attempt has finished."""

    http: Optional[DataAttemptHTTP] = None
    """HTTP request and response information."""

    started_at: Optional[datetime] = None
    """ISO 8601 timestamp indicating when the attempt was initiated."""

    status: Optional[Literal["delivered", "failed"]] = None


class DataWebhook(BaseModel):
    """Original webhook JSON data. Payload fields vary according to event type."""

    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[str] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[Dict[str, object]] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class Data(BaseModel):
    """Record of all attempts to deliver a webhook."""

    id: Optional[str] = None
    """Uniquely identifies the webhook_delivery record."""

    attempts: Optional[List[DataAttempt]] = None
    """Detailed delivery attempts, ordered by most recent."""

    finished_at: Optional[datetime] = None
    """ISO 8601 timestamp indicating when the last webhook response has been received."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    started_at: Optional[datetime] = None
    """ISO 8601 timestamp indicating when the first request attempt was initiated."""

    status: Optional[Literal["delivered", "failed"]] = None
    """
    Delivery status: 'delivered' when successfuly delivered or 'failed' if all
    attempts have failed.
    """

    user_id: Optional[str] = None
    """Uniquely identifies the user that owns the webhook_delivery record."""

    webhook: Optional[DataWebhook] = None
    """Original webhook JSON data. Payload fields vary according to event type."""


class WebhookDeliveryRetrieveResponse(BaseModel):
    data: Optional[Data] = None
    """Record of all attempts to deliver a webhook."""

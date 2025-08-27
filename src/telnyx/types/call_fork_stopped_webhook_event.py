# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CallForkStoppedWebhookEvent", "Data", "DataPayload"]


class DataPayload(BaseModel):
    call_control_id: Optional[str] = None
    """Unique ID for controlling the call."""

    call_leg_id: Optional[str] = None
    """ID that is unique to the call and can be used to correlate webhook events."""

    call_session_id: Optional[str] = None
    """
    ID that is unique to the call session and can be used to correlate webhook
    events. Call session is a group of related call legs that logically belong to
    the same phone call, e.g. an inbound and outbound leg of a transferred call.
    """

    client_state: Optional[str] = None
    """State received from a command."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    stream_type: Optional[Literal["decrypted"]] = None
    """Type of media streamed. It can be either 'raw' or 'decrypted'."""


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["call.fork.stopped"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallForkStoppedWebhookEvent(BaseModel):
    data: Optional[Data] = None

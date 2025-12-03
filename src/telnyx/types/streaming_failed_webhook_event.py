# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["StreamingFailedWebhookEvent", "Data", "DataPayload", "DataPayloadStreamParams"]


class DataPayloadStreamParams(BaseModel):
    stream_url: Optional[str] = None
    """The destination WebSocket address where the stream is going to be delivered."""

    track: Optional[Literal["inbound_track", "outbound_track", "both_tracks"]] = None
    """Specifies which track should be streamed."""


class DataPayload(BaseModel):
    call_control_id: Optional[str] = None
    """Call ID used to issue commands via Call Control API."""

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

    failure_reason: Optional[str] = None
    """A short description explaning why the media streaming failed."""

    stream_id: Optional[str] = None
    """Identifies the streaming."""

    stream_params: Optional[DataPayloadStreamParams] = None
    """Streaming parameters as they were originally given to the Call Control API."""

    stream_type: Optional[Literal["websocket", "dialogflow"]] = None
    """The type of stream connection the stream is performing."""


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["streaming.failed"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the resource."""


class StreamingFailedWebhookEvent(BaseModel):
    data: Optional[Data] = None

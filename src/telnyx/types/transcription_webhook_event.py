# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TranscriptionWebhookEvent", "Data", "DataPayload", "DataPayloadTranscriptionData"]


class DataPayloadTranscriptionData(BaseModel):
    confidence: Optional[float] = None
    """Speech recognition confidence level."""

    is_final: Optional[bool] = None
    """When false, it means that this is an interim result."""

    transcript: Optional[str] = None
    """Recognized text."""

    transcription_track: Optional[Literal["inbound", "outbound"]] = None
    """Indicates which leg of the call has been transcribed.

    This is only available when `transcription_engine` is set to `B`.
    """


class DataPayload(BaseModel):
    call_control_id: Optional[str] = None
    """Unique identifier and token for controlling the call."""

    call_leg_id: Optional[str] = None
    """ID that is unique to the call and can be used to correlate webhook events."""

    call_session_id: Optional[str] = None
    """
    ID that is unique to the call session and can be used to correlate webhook
    events. Call session is a group of related call legs that logically belong to
    the same phone call, e.g. an inbound and outbound leg of a transferred call.
    """

    client_state: Optional[str] = None
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    transcription_data: Optional[DataPayloadTranscriptionData] = None


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["call.transcription"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class TranscriptionWebhookEvent(BaseModel):
    data: Optional[Data] = None

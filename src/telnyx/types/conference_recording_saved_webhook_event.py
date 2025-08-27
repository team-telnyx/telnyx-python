# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ConferenceRecordingSavedWebhookEvent",
    "Data",
    "DataPayload",
    "DataPayloadPublicRecordingURLs",
    "DataPayloadRecordingURLs",
]


class DataPayloadPublicRecordingURLs(BaseModel):
    mp3: Optional[str] = None
    """Recording URL in requested `mp3` format."""

    wav: Optional[str] = None
    """Recording URL in requested `wav` format."""


class DataPayloadRecordingURLs(BaseModel):
    mp3: Optional[str] = None
    """Recording URL in requested `mp3` format."""

    wav: Optional[str] = None
    """Recording URL in requested `wav` format."""


class DataPayload(BaseModel):
    call_control_id: Optional[str] = None
    """Participant's call ID used to issue commands via Call Control API."""

    call_session_id: Optional[str] = None
    """
    ID that is unique to the call session and can be used to correlate webhook
    events. Call session is a group of related call legs that logically belong to
    the same phone call, e.g. an inbound and outbound leg of a transferred call.
    """

    channels: Optional[Literal["single", "dual"]] = None
    """Whether recording was recorded in `single` or `dual` channel."""

    client_state: Optional[str] = None
    """State received from a command."""

    conference_id: Optional[str] = None
    """ID of the conference that is being recorded."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    format: Optional[Literal["wav", "mp3"]] = None
    """The audio file format used when storing the call recording.

    Can be either `mp3` or `wav`.
    """

    public_recording_urls: Optional[DataPayloadPublicRecordingURLs] = None
    """Recording URLs in requested format.

    The URL is valid for as long as the file exists. For security purposes, this
    feature is activated on a per request basis. Please contact customer support
    with your Account ID to request activation.
    """

    recording_ended_at: Optional[datetime] = None
    """ISO 8601 datetime of when recording ended."""

    recording_id: Optional[str] = None
    """ID of the conference recording."""

    recording_started_at: Optional[datetime] = None
    """ISO 8601 datetime of when recording started."""

    recording_urls: Optional[DataPayloadRecordingURLs] = None
    """Recording URLs in requested format.

    These URLs are valid for 10 minutes. After 10 minutes, you may retrieve
    recordings via API using Reports -> Call Recordings documentation, or via
    Mission Control under Reporting -> Recordings.
    """


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["conference.recording.saved"]] = None
    """The type of event being delivered."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class ConferenceRecordingSavedWebhookEvent(BaseModel):
    data: Optional[Data] = None

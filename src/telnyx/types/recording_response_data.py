# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RecordingResponseData", "DownloadURLs"]


class DownloadURLs(BaseModel):
    mp3: Optional[str] = None
    """Link to download the recording in mp3 format."""

    wav: Optional[str] = None
    """Link to download the recording in wav format."""


class RecordingResponseData(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the recording."""

    call_control_id: Optional[str] = None
    """Unique identifier and token for controlling the call."""

    call_leg_id: Optional[str] = None
    """ID unique to the call leg (used to correlate webhook events)."""

    call_session_id: Optional[str] = None
    """
    ID that is unique to the call session and can be used to correlate webhook
    events. Call session is a group of related call legs that logically belong to
    the same phone call, e.g. an inbound and outbound leg of a transferred call.
    """

    channels: Optional[Literal["single", "dual"]] = None
    """
    When `dual`, the final audio file has the first leg on channel A, and the rest
    on channel B.
    """

    conference_id: Optional[str] = None
    """Uniquely identifies the conference."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    download_urls: Optional[DownloadURLs] = None
    """Links to download the recording files."""

    duration_millis: Optional[int] = None
    """The duration of the recording in milliseconds."""

    record_type: Optional[Literal["recording"]] = None

    recording_ended_at: Optional[str] = None
    """ISO 8601 formatted date of when the recording ended."""

    recording_started_at: Optional[str] = None
    """ISO 8601 formatted date of when the recording started."""

    source: Optional[Literal["conference", "call"]] = None
    """The kind of event that led to this recording being created."""

    status: Optional[Literal["completed"]] = None
    """The status of the recording.

    Only `completed` recordings are currently supported.
    """

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

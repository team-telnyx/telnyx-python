# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RecordingResponseData", "DownloadURLs"]


class DownloadURLs(BaseModel):
    """Links to download the recording files."""

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

    connection_id: Optional[str] = None
    """
    Identifies the Telnyx application (Call Control, TeXML) or SIP connection
    resource associated with this recording.
    """

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    download_urls: Optional[DownloadURLs] = None
    """Links to download the recording files."""

    duration_millis: Optional[int] = None
    """The duration of the recording in milliseconds."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The `from` (caller) number for the call that generated this recording."""

    initiated_by: Optional[str] = None
    """Indicates what triggered the recording.

    Possible values include `DialVerb`, `Conference`, `OutboundAPI`, `Trunking`,
    `RecordVerb`, `StartCallRecordingAPI`, `StartConferenceRecordingAPI`.
    """

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

    to: Optional[str] = None
    """The `to` (callee) number for the call that generated this recording."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

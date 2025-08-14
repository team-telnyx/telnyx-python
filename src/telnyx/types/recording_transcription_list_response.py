# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RecordingTranscriptionListResponse", "Data", "Meta", "MetaCursors"]


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the recording transcription."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    duration_millis: Optional[int] = None
    """The duration of the recording transcription in milliseconds."""

    record_type: Optional[Literal["recording_transcription"]] = None

    recording_id: Optional[str] = None
    """Uniquely identifies the recording associated with this transcription."""

    status: Optional[Literal["in-progress", "completed"]] = None
    """The status of the recording transcription.

    Only `completed` has transcription text available.
    """

    transcription_text: Optional[str] = None
    """The recording's transcribed text."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class MetaCursors(BaseModel):
    after: Optional[str] = None
    """Opaque identifier of next page."""

    before: Optional[str] = None
    """Opaque identifier of previous page."""


class Meta(BaseModel):
    cursors: Optional[MetaCursors] = None

    next: Optional[str] = None
    """Path to next page."""

    previous: Optional[str] = None
    """Path to previous page."""


class RecordingTranscriptionListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None

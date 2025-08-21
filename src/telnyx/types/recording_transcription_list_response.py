# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .recording_transcription import RecordingTranscription

__all__ = ["RecordingTranscriptionListResponse", "Meta", "MetaCursors"]


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
    data: Optional[List[RecordingTranscription]] = None

    meta: Optional[Meta] = None

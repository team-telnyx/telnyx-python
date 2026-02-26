# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.cursor import Cursor
from .recording_transcription import RecordingTranscription

__all__ = ["RecordingTranscriptionListResponse", "Meta"]


class Meta(BaseModel):
    cursors: Optional[Cursor] = None

    next: Optional[str] = None
    """Path to next page."""

    previous: Optional[str] = None
    """Path to previous page."""


class RecordingTranscriptionListResponse(BaseModel):
    data: Optional[List[RecordingTranscription]] = None

    meta: Optional[Meta] = None

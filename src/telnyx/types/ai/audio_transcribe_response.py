# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AudioTranscribeResponse", "Segment"]


class Segment(BaseModel):
    id: float
    """Unique identifier of the segment."""

    end: float
    """End time of the segment in seconds."""

    start: float
    """Start time of the segment in seconds."""

    text: str
    """Text content of the segment."""


class AudioTranscribeResponse(BaseModel):
    text: str
    """The transcribed text for the audio file."""

    duration: Optional[float] = None
    """The duration of the audio file in seconds.

    This is only included if `response_format` is set to `verbose_json`.
    """

    segments: Optional[List[Segment]] = None
    """Segments of the transcribed text and their corresponding details.

    This is only included if `response_format` is set to `verbose_json`.
    """

# Custom code for WebSocket streaming support - persists across codegen runs.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["SttServerEvent", "TranscriptFrame", "ErrorFrame"]


class TranscriptFrame(BaseModel):
    """Server-to-client frame containing a transcription result."""

    type: Optional[Literal["transcript"]] = None
    """Frame type identifier."""

    transcript: Optional[str] = None
    """The transcribed text from the audio."""

    is_final: Optional[bool] = FieldInfo(alias="is_final", default=None)
    """Whether this is a final transcription result.

    When `false`, this is an interim result that may be refined.
    """

    confidence: Optional[float] = None
    """Confidence score of the transcription, ranging from 0 to 1."""

    start: Optional[float] = None
    """Start time offset in seconds."""

    duration: Optional[float] = None
    """Duration in seconds."""

    language: Optional[str] = None
    """Detected language code."""

    speaker: Optional[str] = None
    """Speaker identifier for diarization."""


class ErrorFrame(BaseModel):
    """Server-to-client frame indicating an error during transcription.

    The connection is closed shortly after.
    """

    type: Optional[Literal["error"]] = None
    """Frame type identifier."""

    error: Optional[str] = None
    """Error message describing what went wrong."""


SttServerEvent: TypeAlias = Annotated[
    Union[TranscriptFrame, ErrorFrame], PropertyInfo(discriminator="type")
]

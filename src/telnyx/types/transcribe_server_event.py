# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["TranscribeServerEvent", "TranscriptFrame", "SttErrorFrame"]


class TranscriptFrame(BaseModel):
    """Server-to-client frame containing a transcription result."""

    transcript: str
    """The transcribed text from the audio."""

    type: Literal["transcript"]
    """Frame type identifier."""

    confidence: Optional[float] = None
    """Confidence score of the transcription, ranging from 0 to 1."""

    is_final: Optional[bool] = None
    """Whether this is a final transcription result.

    When `false`, this is an interim result that may be refined.
    """


class SttErrorFrame(BaseModel):
    """Server-to-client frame indicating an error during transcription.

    The connection may be closed shortly after.
    """

    error: str
    """Error message describing what went wrong."""

    type: Literal["error"]
    """Frame type identifier."""


TranscribeServerEvent: TypeAlias = Annotated[Union[TranscriptFrame, SttErrorFrame], PropertyInfo(discriminator="type")]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StreamServerEvent", "AudioChunkFrame", "FinalFrame", "ErrorFrame"]


class AudioChunkFrame(BaseModel):
    """Server-to-client frame containing a base64-encoded audio chunk."""

    audio: Optional[str] = None
    """Base64-encoded audio data.

    May be `null` for providers that use `drop_concatenated_audio` mode (Telnyx
    Natural/NaturalHD, Rime, Minimax, MurfAI, Resemble) — in that case only streamed
    chunks carry audio.
    """

    cached: Optional[bool] = None
    """Whether this audio was served from cache."""

    is_final: Optional[bool] = FieldInfo(alias="isFinal", default=None)
    """Always `false` for audio chunk frames."""

    text: Optional[str] = None
    """The text segment that this audio chunk corresponds to."""

    time_to_first_audio_frame_ms: Optional[int] = FieldInfo(alias="timeToFirstAudioFrameMs", default=None)
    """Milliseconds from the start-of-speech request to the first audio frame.

    Only present on the first audio chunk of a synthesis request.
    """


class FinalFrame(BaseModel):
    """Server-to-client frame indicating synthesis is complete for the current text."""

    audio: None = None
    """Always `null` for the final frame."""

    is_final: Optional[Literal[True]] = FieldInfo(alias="isFinal", default=None)
    """Always `true`."""

    text: Optional[str] = None
    """Empty string."""

    time_to_first_audio_frame_ms: Optional[int] = FieldInfo(alias="timeToFirstAudioFrameMs", default=None)
    """Present if this was the first response frame."""


class ErrorFrame(BaseModel):
    """Server-to-client frame indicating an error during synthesis.

    The connection is closed shortly after.
    """

    error: Optional[str] = None
    """Error message describing what went wrong."""


StreamServerEvent: TypeAlias = Union[AudioChunkFrame, FinalFrame, ErrorFrame]

# Custom code for WebSocket streaming support - persists across codegen runs.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpeechToTextStreamParams"]


class SpeechToTextStreamParams(TypedDict, total=False):
    """Parameters for establishing a speech-to-text WebSocket connection.

    These parameters are passed as query string parameters when
    establishing the WebSocket connection to `/speech-to-text/transcription`.
    """

    transcription_engine: Required[Literal["Azure", "Deepgram", "Google", "Telnyx"]]
    """The transcription engine to use for processing the audio stream.

    Supported engines: Azure, Deepgram, Google, Telnyx.
    """

    input_format: Literal["mp3", "wav", "raw"]
    """The format of the input audio stream.

    Supported formats: mp3, wav, raw.
    """

    language: str
    """The language code for transcription (e.g., 'en-US', 'es-ES')."""

    interim_results: bool
    """Whether to return interim (partial) transcription results.

    When `true`, you will receive non-final transcript frames that may be refined.
    """

    model: str
    """The model to use for transcription (engine-specific).

    Examples: 'deepgram/nova-2', 'deepgram/nova-3', 'openai/whisper-tiny'.
    """

    endpointing: int
    """Silence duration (in milliseconds) that triggers end-of-speech detection."""

    keyterm: str
    """A key term to boost in the transcription."""

    keywords: str
    """Comma-separated list of keywords to boost in the transcription."""

    redact: str
    """Enable redaction of sensitive information from transcription results."""

    sample_rate: int
    """Sample rate in Hz (e.g., 8000, 16000, 44100)."""

    channels: int
    """Number of audio channels (1 for mono, 2 for stereo)."""

    encoding: str
    """Audio encoding (e.g., 'linear16', 'mulaw')."""

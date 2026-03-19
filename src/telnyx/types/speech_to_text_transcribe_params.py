# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpeechToTextTranscribeParams"]


class SpeechToTextTranscribeParams(TypedDict, total=False):
    input_format: Required[Literal["mp3", "wav"]]
    """The format of input audio stream."""

    transcription_engine: Required[Literal["Azure", "Deepgram", "Google", "Telnyx"]]
    """The transcription engine to use for processing the audio stream."""

    endpointing: int
    """Silence duration (in milliseconds) that triggers end-of-speech detection.

    When set, the engine uses this value to determine when a speaker has stopped
    talking. Not all engines support this parameter.
    """

    interim_results: bool
    """Whether to receive interim transcription results."""

    keyterm: str
    """A key term to boost in the transcription.

    The engine will be more likely to recognize this term. Can be specified multiple
    times for multiple terms.
    """

    keywords: str
    """Comma-separated list of keywords to boost in the transcription.

    The engine will prioritize recognition of these words.
    """

    language: str
    """The language spoken in the audio stream."""

    model: Literal[
        "fast",
        "deepgram/nova-2",
        "deepgram/nova-3",
        "latest_long",
        "latest_short",
        "command_and_search",
        "phone_call",
        "video",
        "default",
        "medical_conversation",
        "medical_dictation",
        "openai/whisper-tiny",
        "openai/whisper-large-v3-turbo",
    ]
    """The specific model to use within the selected transcription engine."""

    redact: str
    """
    Enable redaction of sensitive information (e.g., PCI data, SSN) from
    transcription results. Supported values depend on the transcription engine.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpeechToTextRetrieveTranscriptionParams"]


class SpeechToTextRetrieveTranscriptionParams(TypedDict, total=False):
    input_format: Required[Literal["mp3", "wav", "linear16", "linear32"]]
    """The format of input audio stream."""

    transcription_engine: Required[
        Literal[
            "Azure",
            "Deepgram",
            "Google",
            "Telnyx",
            "xAI",
            "Speechmatics",
            "Soniox",
            "Parakeet",
            "Humain",
            "Reson8",
            "Cohere",
        ]
    ]
    """The transcription engine to use for processing the audio stream."""

    endpointing: int
    """Silence duration (in milliseconds) that triggers end-of-speech detection.

    When set, the engine uses this value to determine when a speaker has stopped
    talking. Supported by `xAI`, `Deepgram`, `Google`, `Speechmatics`, and `Soniox`.
    `Soniox` accepts values between 500 and 3000. Other engines may not support this
    parameter.
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
    """The language spoken in the audio stream.

    For `cohere/ar-stt`, this must be `ar` or `en` — unlike other engines, Cohere
    does not auto-detect the language, and rejects unsupported values including
    `auto`; omitting it defaults to `ar`.
    """

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
        "xai/grok-stt",
        "speechmatics/standard",
        "soniox/stt-rt-v4",
        "nvidia/parakeet-v3",
        "humain/realtime",
        "reson8/turns",
        "cohere/ar-stt",
    ]
    """The specific model to use within the selected transcription engine."""

    redact: str
    """
    Enable redaction of sensitive information (e.g., PCI data, SSN) from
    transcription results. Supported values depend on the transcription engine.
    """

    sample_rate: int
    """Audio sample rate in Hz.

    Required when `input_format` is a raw encoding (`linear16`, `linear32`) — those
    formats carry no header metadata. Ignored for container formats (`mp3`, `wav`),
    which self-describe their rate.
    """

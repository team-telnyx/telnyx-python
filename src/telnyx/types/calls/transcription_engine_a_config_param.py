# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

from .google_transcription_language import GoogleTranscriptionLanguage

__all__ = ["TranscriptionEngineAConfigParam", "SpeechContext"]


class SpeechContext(TypedDict, total=False):
    boost: float
    """Boost factor for the speech context."""

    phrases: List[str]


class TranscriptionEngineAConfigParam(TypedDict, total=False):
    enable_speaker_diarization: bool
    """Enables speaker diarization."""

    hints: List[str]
    """Hints to improve transcription accuracy."""

    interim_results: bool
    """Whether to send also interim results.

    If set to false, only final results will be sent.
    """

    language: GoogleTranscriptionLanguage
    """Language to use for speech recognition"""

    max_speaker_count: int
    """Defines maximum number of speakers in the conversation."""

    min_speaker_count: int
    """Defines minimum number of speakers in the conversation."""

    model: Literal[
        "latest_long",
        "latest_short",
        "command_and_search",
        "phone_call",
        "video",
        "default",
        "medical_conversation",
        "medical_dictation",
    ]
    """The model to use for transcription."""

    profanity_filter: bool
    """Enables profanity_filter."""

    speech_context: Iterable[SpeechContext]
    """Speech context to improve transcription accuracy."""

    transcription_engine: Literal["A"]
    """Engine identifier for Google transcription service"""

    use_enhanced: bool
    """Enables enhanced transcription, this works for models `phone_call` and `video`."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TranscriptionEngineXaiConfigParam"]


class TranscriptionEngineXaiConfigParam(TypedDict, total=False):
    interim_results: bool
    """Whether to send also interim results.

    If set to false, only final results will be sent.
    """

    language: Literal[
        "ar",
        "cs",
        "da",
        "de",
        "en",
        "es",
        "fa",
        "fil",
        "fr",
        "hi",
        "id",
        "it",
        "ja",
        "ko",
        "mk",
        "ms",
        "nl",
        "pl",
        "pt",
        "ro",
        "ru",
        "sv",
        "th",
        "tr",
        "vi",
    ]
    """Language to use for speech recognition"""

    transcription_engine: Literal["xAI"]
    """Engine identifier for xAI transcription service"""

    transcription_model: Literal["xai/grok-stt"]
    """The model to use for transcription."""

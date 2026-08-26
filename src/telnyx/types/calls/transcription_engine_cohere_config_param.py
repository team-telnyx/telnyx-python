# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TranscriptionEngineCohereConfigParam"]


class TranscriptionEngineCohereConfigParam(TypedDict, total=False):
    language: Literal["ar", "en"]
    """The language of the audio to be transcribed.

    Unlike other self-hosted models, Cohere does not auto-detect the language;
    `auto` is not supported.
    """

    transcription_engine: Literal["Cohere"]
    """Engine identifier for Cohere transcription service"""

    transcription_model: Literal["cohere/ar-stt"]
    """The model to use for transcription."""

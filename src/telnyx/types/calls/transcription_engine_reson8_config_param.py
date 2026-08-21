# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TranscriptionEngineReson8ConfigParam"]


class TranscriptionEngineReson8ConfigParam(TypedDict, total=False):
    language: Literal["auto", "nl", "en", "fr", "fy", "de", "it", "pl", "pt", "es", "sv"]
    """The language of the audio to be transcribed.

    `auto` (the default, also applied when `language` is omitted) enables automatic
    language detection.
    """

    transcription_engine: Literal["Reson8"]
    """Engine identifier for Reson8 transcription service"""

    transcription_model: Literal["reson8/turns"]
    """The model to use for transcription."""

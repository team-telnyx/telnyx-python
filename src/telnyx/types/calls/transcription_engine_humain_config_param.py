# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TranscriptionEngineHumainConfigParam"]


class TranscriptionEngineHumainConfigParam(TypedDict, total=False):
    language: Literal["ar", "en", "codeswitch", "auto"]
    """The language of the audio to be transcribed.

    `codeswitch` enables Arabic/English code-switching. `auto` resolves server-side
    to code-switching.
    """

    transcription_engine: Literal["Humain"]
    """Engine identifier for Humain transcription service"""

    transcription_model: Literal["humain/realtime"]
    """The model to use for transcription."""

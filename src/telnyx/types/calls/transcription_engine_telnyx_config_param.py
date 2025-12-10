# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .telnyx_transcription_language import TelnyxTranscriptionLanguage

__all__ = ["TranscriptionEngineTelnyxConfigParam"]


class TranscriptionEngineTelnyxConfigParam(TypedDict, total=False):
    language: TelnyxTranscriptionLanguage
    """Language to use for speech recognition"""

    transcription_engine: Literal["Telnyx"]
    """Engine identifier for Telnyx transcription service"""

    transcription_model: Literal["openai/whisper-tiny", "openai/whisper-large-v3-turbo"]
    """The model to use for transcription."""

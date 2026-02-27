# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TextToSpeechListVoicesResponse", "Voice"]


class Voice(BaseModel):
    """A voice available for text-to-speech synthesis."""

    gender: Optional[str] = None
    """Voice gender."""

    language: Optional[str] = None
    """Language code."""

    name: Optional[str] = None
    """Voice name."""

    provider: Optional[str] = None
    """The TTS provider."""

    voice_id: Optional[str] = None
    """Voice identifier."""


class TextToSpeechListVoicesResponse(BaseModel):
    """List of available voices."""

    voices: Optional[List[Voice]] = None

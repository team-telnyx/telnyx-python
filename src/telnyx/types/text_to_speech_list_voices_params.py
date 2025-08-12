# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TextToSpeechListVoicesParams"]


class TextToSpeechListVoicesParams(TypedDict, total=False):
    elevenlabs_api_key_ref: str
    """Reference to your ElevenLabs API key stored in the Telnyx Portal"""

    provider: Literal["aws", "azure", "elevenlabs", "telnyx"]
    """Filter voices by provider"""

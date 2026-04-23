# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TextToSpeechListVoicesParams"]


class TextToSpeechListVoicesParams(TypedDict, total=False):
    api_key: str
    """API key for providers that require one to list voices (e.g. ElevenLabs)."""

    provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "rime", "resemble", "xai"]
    """Filter voices by provider. If omitted, voices from all providers are returned."""

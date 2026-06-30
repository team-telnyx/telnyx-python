# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["TextToSpeechGenerateSpeechResponse"]


class TextToSpeechGenerateSpeechResponse(BaseModel):
    """Response when `output_type` is `base64_output`."""

    base64_audio: Optional[str] = None
    """Base64-encoded audio data."""

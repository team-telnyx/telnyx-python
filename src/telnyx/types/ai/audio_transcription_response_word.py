# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["AudioTranscriptionResponseWord"]


class AudioTranscriptionResponseWord(BaseModel):
    """Word-level timing detail.

    Only present when using a `deepgram/*` model with `model_config` options that enable word timestamps.
    """

    end: float
    """End time of the word in seconds."""

    start: float
    """Start time of the word in seconds."""

    word: str
    """The transcribed word."""

    confidence: Optional[float] = None
    """Confidence score for the word (0.0 to 1.0)."""

    punctuated_word: Optional[str] = None
    """The transcribed word with punctuation and capitalisation applied.

    Only present when `punctuate` or `smart_format` is enabled via `model_config`.
    """

    speaker: Optional[int] = None
    """Speaker index. Only present when diarization is enabled via `model_config`."""

    speaker_confidence: Optional[float] = None
    """Confidence score for the speaker assignment (0.0 to 1.0).

    Only present when diarization is enabled via `model_config`.
    """

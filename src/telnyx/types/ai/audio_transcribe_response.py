# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AudioTranscribeResponse", "Segment", "Word"]


class Segment(BaseModel):
    id: float
    """Unique identifier of the segment."""

    end: float
    """End time of the segment in seconds."""

    start: float
    """Start time of the segment in seconds."""

    text: str
    """Text content of the segment."""


class Word(BaseModel):
    """Word-level timing detail.

    Only present when using `deepgram/nova-3` with `model_config` options that enable word timestamps.
    """

    end: float
    """End time of the word in seconds."""

    start: float
    """Start time of the word in seconds."""

    word: str
    """The transcribed word."""

    confidence: Optional[float] = None
    """Confidence score for the word (0.0 to 1.0)."""

    speaker: Optional[int] = None
    """Speaker index. Only present when diarization is enabled via `model_config`."""


class AudioTranscribeResponse(BaseModel):
    """Response fields vary by model.

    `distil-whisper/distil-large-v2` returns `text`, `duration`, and `segments` in `verbose_json` mode. `openai/whisper-large-v3-turbo` returns `text` only. `deepgram/nova-3` returns `text` and, depending on `model_config`, may include `words` with per-word timestamps and speaker labels.
    """

    text: str
    """The transcribed text for the audio file."""

    duration: Optional[float] = None
    """The duration of the audio file in seconds.

    Returned by `distil-whisper/distil-large-v2` and `deepgram/nova-3` when
    `response_format` is `verbose_json`. Not returned by
    `openai/whisper-large-v3-turbo`.
    """

    segments: Optional[List[Segment]] = None
    """Segments of the transcribed text and their corresponding details.

    Returned by `distil-whisper/distil-large-v2` when `response_format` is
    `verbose_json`. Not returned by `openai/whisper-large-v3-turbo`.
    """

    words: Optional[List[Word]] = None
    """Word-level timestamps and optional speaker labels.

    Only returned by `deepgram/nova-3` when word-level output is enabled via
    `model_config`.
    """

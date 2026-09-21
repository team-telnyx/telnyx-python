# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .audio_transcription_response_word import AudioTranscriptionResponseWord

__all__ = ["AudioTranscribeResponse", "Segment"]


class Segment(BaseModel):
    id: float
    """Unique identifier of the segment."""

    end: float
    """End time of the segment in seconds."""

    start: float
    """Start time of the segment in seconds."""

    text: str
    """Text content of the segment."""

    speakers: Optional[List[int]] = None
    """Speaker indices heard in this segment.

    Returned by the `deepgram/*` models when `diarize` is enabled via
    `model_config`.
    """

    words: Optional[List[AudioTranscriptionResponseWord]] = None
    """Word-level timing detail for this segment.

    Returned by the `deepgram/*` models when word-level output is enabled via
    `model_config`.
    """


class AudioTranscribeResponse(BaseModel):
    """Response fields vary by model.

    `distil-whisper/distil-large-v2` returns `text`, `duration`, and `segments` in `verbose_json` mode. `openai/whisper-large-v3-turbo` returns `text` only. The `deepgram/*` models return `text` and, depending on `model_config`, may include `words` with per-word timestamps and speaker labels.
    """

    text: str
    """The transcribed text for the audio file."""

    duration: Optional[float] = None
    """The duration of the audio file in seconds.

    Returned by `distil-whisper/distil-large-v2` and the `deepgram/*` models when
    `response_format` is `verbose_json`. Not returned by
    `openai/whisper-large-v3-turbo`.
    """

    segments: Optional[List[Segment]] = None
    """Segments of the transcribed text and their corresponding details.

    Returned by `distil-whisper/distil-large-v2` and the `deepgram/*` models when
    `response_format` is `verbose_json`; Deepgram segments also carry nested `words`
    and `speakers`. Not returned by `openai/whisper-large-v3-turbo`.
    """

    words: Optional[List[AudioTranscriptionResponseWord]] = None
    """Word-level timestamps and optional speaker labels.

    Only returned by the `deepgram/*` models when word-level output is enabled via
    `model_config`.
    """

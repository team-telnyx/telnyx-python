# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .start_speaking_plan import StartSpeakingPlan

__all__ = ["InferenceEmbeddingInterruptionSettings"]


class InferenceEmbeddingInterruptionSettings(BaseModel):
    """
    Settings for interruptions and how the assistant decides the user has finished speaking. These timings are most relevant when using non turn-taking transcription models. For turn-taking models like `deepgram/flux`, end-of-turn behavior is controlled by the transcription end-of-turn settings under `transcription.settings` (`eot_threshold`, `eot_timeout_ms`, `eager_eot_threshold`).
    """

    disable_greeting_interruption: Optional[bool] = None
    """When true, disables user interruptions while the assistant greeting is playing."""

    enable: Optional[bool] = None
    """Whether users can interrupt the assistant while it is speaking."""

    interrupt_prediction_threshold: Optional[float] = None
    """Interrupt-prediction sensitivity, from 0.0 to 1.0.

    Set to null or 0.0 to disable interrupt prediction.
    """

    start_speaking_plan: Optional[StartSpeakingPlan] = None
    """Controls when the assistant starts speaking after the user stops.

    These thresholds primarily apply to non turn-taking transcription models. For
    turn-taking models like `deepgram/flux`, end-of-turn detection is driven by the
    transcription end-of-turn settings under `transcription.settings` instead.

    Sending any `start_speaking_plan` object — an empty `{}` included (the stored
    config fills in field defaults) — engages per-turn transcript matching: on each
    turn the transcript tail is evaluated against the configured
    `transcription_endpointing_plan` tiers, and the wait is set to the matching
    tier's seconds. When the transcript ends without terminal punctuation or a
    number and `transcription_endpointing_plan` is set, its
    `on_no_punctuation_seconds` tier applies. Only when no tier matches
    (`transcription_endpointing_plan` unset or null) does the wait stay on
    `wait_seconds`. Setting `start_speaking_plan` to `null` (or omitting it) turns
    per-turn matching off entirely, and the assistant starts speaking as soon as
    silence is detected.
    """

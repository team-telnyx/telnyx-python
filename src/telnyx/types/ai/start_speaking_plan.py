# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .transcription_endpointing_plan import TranscriptionEndpointingPlan

__all__ = ["StartSpeakingPlan"]


class StartSpeakingPlan(BaseModel):
    """Controls when the assistant starts speaking after the user stops.

    These thresholds primarily apply to non turn-taking transcription models. For turn-taking models like `deepgram/flux`, end-of-turn detection is driven by the transcription end-of-turn settings under `transcription.settings` instead.

    Sending any `start_speaking_plan` object — an empty `{}` included (the stored config fills in field defaults) — engages per-turn transcript matching: on each turn the transcript tail is evaluated against the configured `transcription_endpointing_plan` tiers, and the wait is set to the matching tier's seconds. When the transcript ends without terminal punctuation or a number and `transcription_endpointing_plan` is set, its `on_no_punctuation_seconds` tier applies. Only when no tier matches (`transcription_endpointing_plan` unset or null) does the wait stay on `wait_seconds`. Setting `start_speaking_plan` to `null` (or omitting it) turns per-turn matching off entirely, and the assistant starts speaking as soon as silence is detected.
    """

    transcription_endpointing_plan: Optional[TranscriptionEndpointingPlan] = None
    """Endpointing thresholds used to decide when the user has finished speaking.

    Applies to non turn-taking transcription models. For `deepgram/flux`, use
    `transcription.settings.eot_threshold` / `eot_timeout_ms` /
    `eager_eot_threshold`. Evaluated per turn, on each caller transcript, only while
    `start_speaking_plan` is present: the tier whose suffix matches the transcript
    tail is applied (a transcript with no terminal punctuation or number falls
    through to `on_no_punctuation_seconds`); with no tiers configured (or a null
    nested plan), the per-turn wait stays on `start_speaking_plan.wait_seconds`.
    """

    wait_seconds: Optional[float] = None
    """Wait used when per-turn endpointing does not select a tier.

    While the plan is present this applies on every turn without a matching tier
    (including when `transcription_endpointing_plan` is unset); a matching tier
    replaces it for that turn, and a tier may be shorter or longer than this value.
    """

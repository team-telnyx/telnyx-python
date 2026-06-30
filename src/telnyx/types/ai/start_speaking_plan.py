# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .transcription_endpointing_plan import TranscriptionEndpointingPlan

__all__ = ["StartSpeakingPlan"]


class StartSpeakingPlan(BaseModel):
    """Controls when the assistant starts speaking after the user stops.

    These thresholds primarily apply to non turn-taking transcription models. For turn-taking models like `deepgram/flux`, end-of-turn detection is driven by the transcription end-of-turn settings under `transcription.settings` instead.
    """

    transcription_endpointing_plan: Optional[TranscriptionEndpointingPlan] = None
    """Endpointing thresholds used to decide when the user has finished speaking.

    Applies to non turn-taking transcription models. For `deepgram/flux`, use
    `transcription.settings.eot_threshold` / `eot_timeout_ms` /
    `eager_eot_threshold`.
    """

    wait_seconds: Optional[float] = None
    """Minimum seconds to wait before the assistant starts speaking."""

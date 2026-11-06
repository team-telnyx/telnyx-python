# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["TranscriptionEndpointingPlan"]


class TranscriptionEndpointingPlan(BaseModel):
    """Endpointing thresholds used to decide when the user has finished speaking.

    Applies to non turn-taking transcription models. For `deepgram/flux`, use `transcription.settings.eot_threshold` / `eot_timeout_ms` / `eager_eot_threshold`. Evaluated per turn, on each caller transcript, only while `start_speaking_plan` is present: the tier whose suffix matches the transcript tail is applied (a transcript with no terminal punctuation or number falls through to `on_no_punctuation_seconds`); with no tiers configured (or a null nested plan), the per-turn wait stays on `start_speaking_plan.wait_seconds`.
    """

    on_no_punctuation_seconds: Optional[float] = None
    """Seconds to wait after the transcript ends without punctuation."""

    on_number_seconds: Optional[float] = None
    """Seconds to wait after the transcript ends with a number."""

    on_punctuation_seconds: Optional[float] = None
    """Seconds to wait after the transcript ends with punctuation."""

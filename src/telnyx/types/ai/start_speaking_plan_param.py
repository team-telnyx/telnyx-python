# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .transcription_endpointing_plan_param import TranscriptionEndpointingPlanParam

__all__ = ["StartSpeakingPlanParam"]


class StartSpeakingPlanParam(TypedDict, total=False):
    """Controls when the assistant starts speaking after the user stops.

    These thresholds primarily apply to non turn-taking transcription models. For turn-taking models like `deepgram/flux`, end-of-turn detection is driven by the transcription end-of-turn settings under `transcription.settings` instead.
    """

    transcription_endpointing_plan: TranscriptionEndpointingPlanParam
    """Endpointing thresholds used to decide when the user has finished speaking.

    Applies to non turn-taking transcription models. For `deepgram/flux`, use
    `transcription.settings.eot_threshold` / `eot_timeout_ms` /
    `eager_eot_threshold`.
    """

    wait_seconds: float
    """Minimum seconds to wait before the assistant starts speaking."""

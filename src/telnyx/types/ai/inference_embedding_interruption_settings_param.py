# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .start_speaking_plan_param import StartSpeakingPlanParam

__all__ = ["InferenceEmbeddingInterruptionSettingsParam"]


class InferenceEmbeddingInterruptionSettingsParam(TypedDict, total=False):
    """
    Settings for interruptions and how the assistant decides the user has finished speaking. These timings are most relevant when using non turn-taking transcription models. For turn-taking models like `deepgram/flux`, end-of-turn behavior is controlled by the transcription end-of-turn settings under `transcription.settings` (`eot_threshold`, `eot_timeout_ms`, `eager_eot_threshold`).
    """

    enable: bool
    """Whether users can interrupt the assistant while it is speaking."""

    start_speaking_plan: StartSpeakingPlanParam
    """Controls when the assistant starts speaking after the user stops.

    These thresholds primarily apply to non turn-taking transcription models. For
    turn-taking models like `deepgram/flux`, end-of-turn detection is driven by the
    transcription end-of-turn settings under `transcription.settings` instead.
    """

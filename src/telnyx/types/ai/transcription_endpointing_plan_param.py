# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TranscriptionEndpointingPlanParam"]


class TranscriptionEndpointingPlanParam(TypedDict, total=False):
    """Endpointing thresholds used to decide when the user has finished speaking.

    Applies to non turn-taking transcription models. For `deepgram/flux`, use `transcription.settings.eot_threshold` / `eot_timeout_ms` / `eager_eot_threshold`.
    """

    on_no_punctuation_seconds: float
    """Seconds to wait after the transcript ends without punctuation."""

    on_number_seconds: float
    """Seconds to wait after the transcript ends with a number."""

    on_punctuation_seconds: float
    """Seconds to wait after the transcript ends with punctuation."""

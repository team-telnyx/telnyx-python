# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TranscriptionEngineSonioxConfigParam"]


class TranscriptionEngineSonioxConfigParam(TypedDict, total=False):
    transcription_engine: Required[Literal["Soniox"]]
    """Engine identifier for Soniox transcription service"""

    enable_endpoint_detection: bool
    """
    When true, Soniox emits end-of-utterance events at the cadence configured by
    `max_endpoint_delay_ms`.
    """

    interim_results: bool
    """Whether to send also interim results.

    If set to false, only final results will be sent.
    """

    language: str
    """ISO 639-1 language hint (e.g.

    `en`, `es`), or `auto` to omit the hint and let Soniox auto-detect supported
    languages multilingually.
    """

    max_endpoint_delay_ms: int
    """Maximum silence (in milliseconds) before Soniox emits an end-of-utterance event.

    Only honored when `enable_endpoint_detection` is true. Range: 500-3000 ms.
    """

    transcription_model: Literal["soniox/stt-rt-v4"]
    """The model to use for transcription."""

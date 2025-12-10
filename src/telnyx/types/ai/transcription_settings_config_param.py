# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TranscriptionSettingsConfigParam"]


class TranscriptionSettingsConfigParam(TypedDict, total=False):
    eot_threshold: float
    """Available only for deepgram/flux.

    Confidence required to trigger an end of turn. Higher values = more reliable
    turn detection but slightly increased latency.
    """

    eot_timeout_ms: int
    """Available only for deepgram/flux.

    Maximum milliseconds of silence before forcing an end of turn, regardless of
    confidence.
    """

    numerals: bool

    smart_format: bool

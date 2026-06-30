# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["DeepgramNova3ConfigParam"]


class DeepgramNova3ConfigParam(TypedDict, total=False):
    transcription_engine: Required[Literal["deepgram/nova-3"]]

    transcription_model: Required[Literal["deepgram/nova-3"]]

    interim_results: bool
    """Whether to send also interim results.

    If set to false, only final results will be sent.
    """

    keyterms: SequenceNotStr[str]
    """Nova-3 keyterm prompting.

    Up to 100 domain-specific terms or brand names to bias recognition toward.
    Nova-3-only; use `hints` on Nova-2.
    """

    keywords_boosting: Dict[str, float]
    """
    Keywords and their respective intensifiers (boosting values) to improve
    transcription accuracy for specific words or phrases. The intensifier should be
    a numeric value. Example: `{"snuffleupagus": 5, "systrom": 2, "krieger": 1}`.
    """

    language: Literal[
        "en-US",
        "en-AU",
        "en-GB",
        "en-IN",
        "en-NZ",
        "de",
        "nl",
        "sv-SE",
        "da-DK",
        "es",
        "es-419",
        "fr",
        "fr-CA",
        "pt-BR",
        "pt-PT",
        "auto_detect",
    ]
    """Language to use for speech recognition with nova-3 model"""

    smart_format: bool
    """
    Enable Deepgram's smart formatting (capitalization, punctuation, and digit
    normalization). Note: Telnyx defaults this to `true`, overriding Deepgram's
    underlying default of `false` — omit the field to get a smart-formatted
    transcript, or set it to `false` to receive the raw lowercase transcript without
    punctuation.
    """

    utterance_end_ms: int
    """Number of milliseconds of silence to consider an utterance ended.

    Ranges from 0 to 5000 ms.
    """

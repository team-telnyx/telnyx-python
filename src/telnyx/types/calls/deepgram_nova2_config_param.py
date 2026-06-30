# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["DeepgramNova2ConfigParam"]


class DeepgramNova2ConfigParam(TypedDict, total=False):
    transcription_engine: Required[Literal["deepgram/nova-2"]]

    transcription_model: Required[Literal["deepgram/nova-2"]]

    hints: SequenceNotStr[str]
    """Nova-2 keyword biasing without intensifiers.

    Up to 100 terms to bias recognition toward. For weighted biasing, use
    `keywords_boosting` instead. Nova-2-only; use `keyterms` on Nova-3.
    """

    interim_results: bool
    """Whether to send also interim results.

    If set to false, only final results will be sent.
    """

    keywords_boosting: Dict[str, float]
    """
    Keywords and their respective intensifiers (boosting values) to improve
    transcription accuracy for specific words or phrases. The intensifier should be
    a numeric value. Example: `{"snuffleupagus": 5, "systrom": 2, "krieger": 1}`.
    """

    language: Literal[
        "bg",
        "ca",
        "zh-CN",
        "zh-Hans",
        "zh-TW",
        "zh-Hant",
        "zh-HK",
        "cs",
        "da-DK",
        "nl-BE",
        "en-US",
        "en-AU",
        "en-GB",
        "en-NZ",
        "en-IN",
        "et",
        "fi",
        "fr",
        "fr-CA",
        "de-CH",
        "el",
        "hi",
        "hu",
        "id",
        "it",
        "ja",
        "ko-KR",
        "lv",
        "lt",
        "ms",
        "no",
        "pl",
        "pt-BR",
        "pt-PT",
        "ro",
        "ru",
        "sk",
        "es-419",
        "sv-SE",
        "th-TH",
        "tr",
        "uk",
        "vi",
        "auto_detect",
    ]
    """Language to use for speech recognition with nova-2 model"""

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

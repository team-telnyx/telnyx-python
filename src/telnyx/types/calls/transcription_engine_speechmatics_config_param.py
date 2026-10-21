# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TranscriptionEngineSpeechmaticsConfigParam"]


class TranscriptionEngineSpeechmaticsConfigParam(TypedDict, total=False):
    interim_results: bool
    """Whether to send also interim results.

    If set to false, only final results will be sent.
    """

    language: Literal[
        "en",
        "ba",
        "eu",
        "gl",
        "ga",
        "mt",
        "mn",
        "sw",
        "ug",
        "cy",
        "ar_en",
        "cmn_en",
        "en_ms",
        "en_ta",
        "tl",
        "es-bilingual-en",
        "cmn_en_ms_ta",
        "ar",
        "be",
        "bg",
        "bn",
        "ca",
        "cmn",
        "cs",
        "da",
        "de",
        "el",
        "eo",
        "es",
        "et",
        "fa",
        "fi",
        "fr",
        "he",
        "hi",
        "hr",
        "hu",
        "ia",
        "id",
        "it",
        "ja",
        "ko",
        "lt",
        "lv",
        "mr",
        "ms",
        "nl",
        "no",
        "pl",
        "pt",
        "ro",
        "ru",
        "sk",
        "sl",
        "sv",
        "ta",
        "th",
        "tr",
        "uk",
        "ur",
        "vi",
        "yue",
        "en-US",
        "en-GB",
        "en-AU",
        "cmn-Hans",
        "cmn-Hant",
    ]
    """Language to use for speech recognition.

    Accepted values depend on the selected `transcription_model`.
    `speechmatics/standard` supports: `en`, `ba`, `eu`, `gl`, `ga`, `mt`, `mn`,
    `sw`, `ug`, `cy`, `ar_en`, `cmn_en`, `en_ms`, `en_ta`, `tl`, `es-bilingual-en`,
    `cmn_en_ms_ta`. `speechmatics/linden-1` (preview) supports the same languages as
    Speechmatics Realtime: `ar`, `ar_en`, `ba`, `be`, `bg`, `bn`, `ca`, `cmn`,
    `cmn_en`, `cmn_en_ms_ta`, `cs`, `cy`, `da`, `de`, `el`, `en`, `en_ms`, `en_ta`,
    `eo`, `es`, `es-bilingual-en`, `et`, `eu`, `fa`, `fi`, `fr`, `ga`, `gl`, `he`,
    `hi`, `hr`, `hu`, `ia`, `id`, `it`, `ja`, `ko`, `lt`, `lv`, `mn`, `mr`, `ms`,
    `mt`, `nl`, `no`, `pl`, `pt`, `ro`, `ru`, `sk`, `sl`, `sv`, `sw`, `ta`, `th`,
    `tl`, `tr`, `ug`, `uk`, `ur`, `vi`, `yue`, plus the spelling and script variants
    `en-US`, `en-GB`, `en-AU`, `cmn-Hans`, and `cmn-Hant` (`en` alone uses the
    default spelling). A value outside the selected model's list is rejected. For
    `speechmatics/standard`, unset, blank, `auto`, `auto_beta`, or `multi` defaults
    to `en`; for `speechmatics/linden-1`, only an unset language defaults to `en`,
    and `auto`, `auto_beta`, or `multi` is rejected.
    """

    transcription_engine: Literal["Speechmatics"]
    """Engine identifier for Speechmatics transcription service"""

    transcription_model: Literal["speechmatics/standard", "speechmatics/linden-1"]
    """The model to use for transcription.

    `speechmatics/linden-1` is a preview, vendor-hosted model with its own language
    support (see `language`).
    """

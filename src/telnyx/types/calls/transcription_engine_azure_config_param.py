# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TranscriptionEngineAzureConfigParam"]


class TranscriptionEngineAzureConfigParam(TypedDict, total=False):
    region: Required[Literal["australiaeast", "centralindia", "eastus", "northcentralus", "westeurope", "westus2"]]
    """Azure region to use for speech recognition"""

    transcription_engine: Required[Literal["Azure"]]
    """Engine identifier for Azure transcription service"""

    api_key_ref: str
    """Reference to the API key for authentication.

    See
    [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    for details. The parameter is optional as defaults are available for some
    regions.
    """

    language: Literal[
        "af",
        "am",
        "ar",
        "bg",
        "bn",
        "bs",
        "ca",
        "cs",
        "cy",
        "da",
        "de",
        "el",
        "en",
        "es",
        "et",
        "eu",
        "fa",
        "fi",
        "fr",
        "ga",
        "gl",
        "gu",
        "he",
        "hi",
        "hr",
        "hu",
        "hy",
        "id",
        "is",
        "it",
        "ja",
        "ka",
        "kk",
        "km",
        "kn",
        "ko",
        "lo",
        "lt",
        "lv",
        "mk",
        "ml",
        "mn",
        "mr",
        "ms",
        "mt",
        "my",
        "nb",
        "ne",
        "nl",
        "pl",
        "ps",
        "pt",
        "ro",
        "ru",
        "si",
        "sk",
        "sl",
        "so",
        "sq",
        "sr",
        "sv",
        "sw",
        "ta",
        "te",
        "th",
        "tr",
        "uk",
        "ur",
        "uz",
        "vi",
        "wuu",
        "yue",
        "zh",
        "zu",
        "auto",
    ]
    """Language to use for speech recognition"""

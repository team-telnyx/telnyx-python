# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .transcription_engine_a_config_param import TranscriptionEngineAConfigParam
from .transcription_engine_b_config_param import TranscriptionEngineBConfigParam
from .transcription_engine_azure_config_param import TranscriptionEngineAzureConfigParam
from .transcription_engine_google_config_param import TranscriptionEngineGoogleConfigParam
from .transcription_engine_telnyx_config_param import TranscriptionEngineTelnyxConfigParam

__all__ = [
    "TranscriptionStartRequestParam",
    "TranscriptionEngineConfig",
    "TranscriptionEngineConfigDeepgramNova2Config",
    "TranscriptionEngineConfigDeepgramNova3Config",
]


class TranscriptionEngineConfigDeepgramNova2Config(TypedDict, total=False):
    transcription_engine: Required[Literal["Deepgram"]]

    transcription_model: Required[Literal["deepgram/nova-2"]]

    keywords_boosting: Dict[str, float]
    """
    Keywords and their respective intensifiers (boosting values) to improve
    transcription accuracy for specific words or phrases. The intensifier should be
    a numeric value. Example: `{"snuffleupagus": 5, "systrom": 2, "krieger": 1}`.
    """

    language: Literal[
        "bg",
        "ca",
        "zh",
        "zh-CN",
        "zh-Hans",
        "zh-TW",
        "zh-Hant",
        "zh-HK",
        "cs",
        "da",
        "da-DK",
        "nl",
        "en",
        "en-US",
        "en-AU",
        "en-GB",
        "en-NZ",
        "en-IN",
        "et",
        "fi",
        "nl-BE",
        "fr",
        "fr-CA",
        "de",
        "de-CH",
        "el",
        "hi",
        "hu",
        "id",
        "it",
        "ja",
        "ko",
        "ko-KR",
        "lv",
        "lt",
        "ms",
        "no",
        "pl",
        "pt",
        "pt-BR",
        "pt-PT",
        "ro",
        "ru",
        "sk",
        "es",
        "es-419",
        "sv",
        "sv-SE",
        "th",
        "th-TH",
        "tr",
        "uk",
        "vi",
        "auto_detect",
    ]
    """Language to use for speech recognition with nova-2 model"""


class TranscriptionEngineConfigDeepgramNova3Config(TypedDict, total=False):
    transcription_engine: Required[Literal["Deepgram"]]

    transcription_model: Required[Literal["deepgram/nova-3"]]

    keywords_boosting: Dict[str, float]
    """
    Keywords and their respective intensifiers (boosting values) to improve
    transcription accuracy for specific words or phrases. The intensifier should be
    a numeric value. Example: `{"snuffleupagus": 5, "systrom": 2, "krieger": 1}`.
    """

    language: Literal[
        "en",
        "en-US",
        "en-AU",
        "en-GB",
        "en-IN",
        "en-NZ",
        "de",
        "nl",
        "sv",
        "sv-SE",
        "da",
        "da-DK",
        "es",
        "es-419",
        "fr",
        "fr-CA",
        "pt",
        "pt-BR",
        "pt-PT",
        "auto_detect",
    ]
    """Language to use for speech recognition with nova-3 model"""


TranscriptionEngineConfig: TypeAlias = Union[
    TranscriptionEngineGoogleConfigParam,
    TranscriptionEngineTelnyxConfigParam,
    TranscriptionEngineConfigDeepgramNova2Config,
    TranscriptionEngineConfigDeepgramNova3Config,
    TranscriptionEngineAzureConfigParam,
    TranscriptionEngineAConfigParam,
    TranscriptionEngineBConfigParam,
]


class TranscriptionStartRequestParam(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    transcription_engine: Literal["Google", "Telnyx", "Deepgram", "Azure", "A", "B"]
    """Engine to use for speech recognition.

    Legacy values `A` - `Google`, `B` - `Telnyx` are supported for backward
    compatibility.
    """

    transcription_engine_config: TranscriptionEngineConfig

    transcription_tracks: str
    """Indicates which leg of the call will be transcribed.

    Use `inbound` for the leg that requested the transcription, `outbound` for the
    other leg, and `both` for both legs of the call. Will default to `inbound`.
    """

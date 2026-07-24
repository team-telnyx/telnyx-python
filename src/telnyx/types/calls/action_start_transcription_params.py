# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict

from .deepgram_nova2_config_param import DeepgramNova2ConfigParam
from .deepgram_nova3_config_param import DeepgramNova3ConfigParam
from .transcription_engine_a_config_param import TranscriptionEngineAConfigParam
from .transcription_engine_b_config_param import TranscriptionEngineBConfigParam
from .transcription_engine_xai_config_param import TranscriptionEngineXaiConfigParam
from .transcription_engine_azure_config_param import TranscriptionEngineAzureConfigParam
from .transcription_engine_google_config_param import TranscriptionEngineGoogleConfigParam
from .transcription_engine_soniox_config_param import TranscriptionEngineSonioxConfigParam
from .transcription_engine_telnyx_config_param import TranscriptionEngineTelnyxConfigParam
from .transcription_engine_parakeet_config_param import TranscriptionEngineParakeetConfigParam
from .transcription_engine_assemblyai_config_param import TranscriptionEngineAssemblyaiConfigParam
from .transcription_engine_speechmatics_config_param import TranscriptionEngineSpeechmaticsConfigParam

__all__ = [
    "ActionStartTranscriptionParams",
    "TranscriptionEngineConfig",
    "TranscriptionEngineConfigTranscriptionEngineHumainConfig",
]


class ActionStartTranscriptionParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    transcription_engine: Literal[
        "Google",
        "Telnyx",
        "Deepgram",
        "Azure",
        "xAI",
        "AssemblyAI",
        "Speechmatics",
        "Soniox",
        "Parakeet",
        "Humain",
        "A",
        "B",
    ]
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


class TranscriptionEngineConfigTranscriptionEngineHumainConfig(TypedDict, total=False):
    language: Literal["ar", "en", "codeswitch", "auto"]
    """The language of the audio to be transcribed.

    `codeswitch` enables Arabic/English code-switching. `auto` resolves server-side
    to code-switching.
    """

    transcription_engine: Literal["Humain"]
    """Engine identifier for Humain transcription service"""

    transcription_model: Literal["humain/realtime"]
    """The model to use for transcription."""


TranscriptionEngineConfig: TypeAlias = Union[
    TranscriptionEngineGoogleConfigParam,
    TranscriptionEngineTelnyxConfigParam,
    TranscriptionEngineAzureConfigParam,
    TranscriptionEngineXaiConfigParam,
    TranscriptionEngineAssemblyaiConfigParam,
    TranscriptionEngineSpeechmaticsConfigParam,
    TranscriptionEngineSonioxConfigParam,
    TranscriptionEngineParakeetConfigParam,
    TranscriptionEngineConfigTranscriptionEngineHumainConfig,
    TranscriptionEngineAConfigParam,
    TranscriptionEngineBConfigParam,
    DeepgramNova2ConfigParam,
    DeepgramNova3ConfigParam,
]

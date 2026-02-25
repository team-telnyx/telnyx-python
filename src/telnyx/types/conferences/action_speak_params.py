# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..calls.aws_voice_settings_param import AwsVoiceSettingsParam
from ..calls.telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from ..shared_params.minimax_voice_settings import MinimaxVoiceSettings
from ..calls.eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam

__all__ = [
    "ActionSpeakParams",
    "VoiceSettings",
    "VoiceSettingsAzureVoiceSettings",
    "VoiceSettingsRimeVoiceSettings",
    "VoiceSettingsResembleVoiceSettings",
]


class ActionSpeakParams(TypedDict, total=False):
    payload: Required[str]
    """The text or SSML to be converted into speech. There is a 3,000 character limit."""

    voice: Required[str]
    """Specifies the voice used in speech synthesis.

    - Define voices using the format `<Provider>.<Model>.<VoiceId>`. Specifying only
      the provider will give default values for voice_id and model_id.

      **Supported Providers:**

    - **AWS:** Use `AWS.Polly.<VoiceId>` (e.g., `AWS.Polly.Joanna`). For neural
      voices, which provide more realistic, human-like speech, append `-Neural` to
      the `VoiceId` (e.g., `AWS.Polly.Joanna-Neural`). Check the
      [available voices](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html)
      for compatibility.
    - **Azure:** Use `Azure.<VoiceId>` (e.g., `Azure.en-CA-ClaraNeural`,
      `Azure.en-US-BrianMultilingualNeural`,
      `Azure.en-US-Ava:DragonHDLatestNeural`). For a complete list of voices, go to
      [Azure Voice Gallery](https://speech.microsoft.com/portal/voicegallery). Use
      `voice_settings` to configure custom deployments, regions, or API keys.
    - **ElevenLabs:** Use `ElevenLabs.<ModelId>.<VoiceId>` (e.g.,
      `ElevenLabs.eleven_multilingual_v2.21m00Tcm4TlvDq8ikWAM`). The `ModelId` part
      is optional. To use ElevenLabs, you must provide your ElevenLabs API key as an
      integration identifier secret in
      `"voice_settings": {"api_key_ref": "<secret_identifier>"}`. See
      [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
      for details. Check
      [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
    - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>` (e.g., `Telnyx.KokoroTTS.af`).
      Use `voice_settings` to configure voice_speed and other synthesis parameters.
    - **Minimax:** Use `Minimax.<ModelId>.<VoiceId>` (e.g.,
      `Minimax.speech-02-hd.Wise_Woman`). Supported models: `speech-02-turbo`,
      `speech-02-hd`, `speech-2.6-turbo`, `speech-2.8-turbo`. Use `voice_settings`
      to configure speed, volume, pitch, and language_boost.
    - **Rime:** Use `Rime.<model_id>.<voice_id>` (e.g., `Rime.Arcana.cove`).
      Supported model_ids: `Arcana`, `Mist`. Use `voice_settings` to configure
      voice_speed.
    - **Resemble:** Use `Resemble.Turbo.<voice_id>` (e.g.,
      `Resemble.Turbo.my_voice`). Only `Turbo` model is supported. Use
      `voice_settings` to configure precision, sample_rate, and format.

    For service_level basic, you may define the gender of the speaker (male or
    female).
    """

    call_control_ids: SequenceNotStr[str]
    """Call Control IDs of participants who will hear the spoken text.

    When empty all participants will hear the spoken text.
    """

    command_id: str
    """Use this field to avoid execution of duplicate commands.

    Telnyx will ignore subsequent commands with the same `command_id` as one that
    has already been executed.
    """

    language: Literal[
        "arb",
        "cmn-CN",
        "cy-GB",
        "da-DK",
        "de-DE",
        "en-AU",
        "en-GB",
        "en-GB-WLS",
        "en-IN",
        "en-US",
        "es-ES",
        "es-MX",
        "es-US",
        "fr-CA",
        "fr-FR",
        "hi-IN",
        "is-IS",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "nb-NO",
        "nl-NL",
        "pl-PL",
        "pt-BR",
        "pt-PT",
        "ro-RO",
        "ru-RU",
        "sv-SE",
        "tr-TR",
    ]
    """The language you want spoken.

    This parameter is ignored when a `Polly.*` voice is specified.
    """

    payload_type: Literal["text", "ssml"]
    """The type of the provided payload.

    The payload can either be plain text, or Speech Synthesis Markup Language
    (SSML).
    """

    region: Literal["Australia", "Europe", "Middle East", "US"]
    """Region where the conference data is located.

    Defaults to the region defined in user's data locality settings (Europe or US).
    """

    voice_settings: VoiceSettings
    """The settings associated with the voice selected"""


class VoiceSettingsAzureVoiceSettings(TypedDict, total=False):
    type: Required[Literal["azure"]]
    """Voice settings provider type"""

    api_key_ref: str
    """
    The `identifier` for an integration secret that refers to your Azure Speech API
    key.
    """

    deployment_id: str
    """The deployment ID for a custom Azure neural voice."""

    effect: Literal["eq_car", "eq_telecomhp8k"]
    """Audio effect to apply."""

    gender: Literal["Male", "Female"]
    """Voice gender filter."""

    region: str
    """The Azure region for the Speech service (e.g., `eastus`, `westeurope`).

    Required when using a custom API key.
    """


class VoiceSettingsRimeVoiceSettings(TypedDict, total=False):
    type: Required[Literal["rime"]]
    """Voice settings provider type"""

    voice_speed: float
    """Speech speed multiplier. Default is 1.0."""


class VoiceSettingsResembleVoiceSettings(TypedDict, total=False):
    type: Required[Literal["resemble"]]
    """Voice settings provider type"""

    format: Literal["wav", "mp3"]
    """Output audio format."""

    precision: Literal["PCM_16", "PCM_24", "PCM_32", "MULAW"]
    """Audio precision format."""

    sample_rate: Literal["8000", "16000", "22050", "32000", "44100", "48000"]
    """Audio sample rate in Hz."""


VoiceSettings: TypeAlias = Union[
    ElevenLabsVoiceSettingsParam,
    TelnyxVoiceSettingsParam,
    AwsVoiceSettingsParam,
    MinimaxVoiceSettings,
    VoiceSettingsAzureVoiceSettings,
    VoiceSettingsRimeVoiceSettings,
    VoiceSettingsResembleVoiceSettings,
]

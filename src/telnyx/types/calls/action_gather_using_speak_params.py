# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .aws_voice_settings_param import AwsVoiceSettingsParam
from .telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from .eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam

__all__ = ["ActionGatherUsingSpeakParams", "VoiceSettings"]


class ActionGatherUsingSpeakParams(TypedDict, total=False):
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
    - **Azure:** Use `Azure.<VoiceId>. (e.g. Azure.en-CA-ClaraNeural,
      Azure.en-CA-LiamNeural, Azure.en-US-BrianMultilingualNeural,
      Azure.en-US-Ava:DragonHDLatestNeural. For a complete list of voices, go to
      [Azure Voice Gallery](https://speech.microsoft.com/portal/voicegallery).)
    - **ElevenLabs:** Use `ElevenLabs.<ModelId>.<VoiceId>` (e.g.,
      `ElevenLabs.eleven_multilingual_v2.21m00Tcm4TlvDq8ikWAM`). The `ModelId` part
      is optional. To use ElevenLabs, you must provide your ElevenLabs API key as an
      integration identifier secret in
      `"voice_settings": {"api_key_ref": "<secret_identifier>"}`. See
      [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
      for details. Check
      [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
    - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>`

    For service_level basic, you may define the gender of the speaker (male or
    female).
    """

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    inter_digit_timeout_millis: int
    """The number of milliseconds to wait for input between digits."""

    invalid_payload: str
    """
    The text or SSML to be converted into speech when digits don't match the
    `valid_digits` parameter or the number of digits is not between `min` and `max`.
    There is a 3,000 character limit.
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

    maximum_digits: int
    """The maximum number of digits to fetch.

    This parameter has a maximum value of 128.
    """

    maximum_tries: int
    """
    The maximum number of times that a file should be played back if there is no
    input from the user on the call.
    """

    minimum_digits: int
    """The minimum number of digits to fetch. This parameter has a minimum value of 1."""

    payload_type: Literal["text", "ssml"]
    """The type of the provided payload.

    The payload can either be plain text, or Speech Synthesis Markup Language
    (SSML).
    """

    service_level: Literal["basic", "premium"]
    """This parameter impacts speech quality, language options and payload types.

    When using `basic`, only the `en-US` language and payload type `text` are
    allowed.
    """

    terminating_digit: str
    """
    The digit used to terminate input if fewer than `maximum_digits` digits have
    been gathered.
    """

    timeout_millis: int
    """
    The number of milliseconds to wait for a DTMF response after speak ends before a
    replaying the sound file.
    """

    valid_digits: str
    """A list of all digits accepted as valid."""

    voice_settings: VoiceSettings
    """The settings associated with the voice selected"""


VoiceSettings: TypeAlias = Union[ElevenLabsVoiceSettingsParam, TelnyxVoiceSettingsParam, AwsVoiceSettingsParam]

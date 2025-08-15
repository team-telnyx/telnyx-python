# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..ai.assistant_param import AssistantParam
from .aws_voice_settings_param import AwsVoiceSettingsParam
from .transcription_config_param import TranscriptionConfigParam
from .interruption_settings_param import InterruptionSettingsParam
from .telnyx_voice_settings_param import TelnyxVoiceSettingsParam
from .google_transcription_language import GoogleTranscriptionLanguage
from .eleven_labs_voice_settings_param import ElevenLabsVoiceSettingsParam

__all__ = ["ActionGatherUsingAIParams", "MessageHistory", "VoiceSettings"]


class ActionGatherUsingAIParams(TypedDict, total=False):
    parameters: Required[object]
    """
    The parameters described as a JSON Schema object that needs to be gathered by
    the voice assistant. See the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema) for
    documentation about the format
    """

    assistant: AssistantParam
    """
    Assistant configuration including choice of LLM, custom instructions, and tools.
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

    greeting: str
    """
    Text that will be played when the gathering starts, if none then nothing will be
    played when the gathering starts. The greeting can be text for any voice or SSML
    for `AWS.Polly.<voice_id>` voices. There is a 3,000 character limit.
    """

    interruption_settings: InterruptionSettingsParam
    """Settings for handling user interruptions during assistant speech"""

    language: GoogleTranscriptionLanguage
    """Language to use for speech recognition"""

    message_history: Iterable[MessageHistory]
    """
    The message history you want the voice assistant to be aware of, this can be
    useful to keep the context of the conversation, or to pass additional
    information to the voice assistant.
    """

    send_message_history_updates: bool
    """Default is `false`.

    If set to `true`, the voice assistant will send updates to the message history
    via the `call.ai_gather.message_history_updated`
    [callback](https://developers.telnyx.com/api/call-control/call-gather-using-ai#callbacks)
    in real time as the message history is updated.
    """

    send_partial_results: bool
    """Default is `false`.

    If set to `true`, the voice assistant will send partial results via the
    `call.ai_gather.partial_results`
    [callback](https://developers.telnyx.com/api/call-control/call-gather-using-ai#callbacks)
    in real time as individual fields are gathered. If set to `false`, the voice
    assistant will only send the final result via the `call.ai_gather.ended`
    callback.
    """

    transcription: TranscriptionConfigParam
    """The settings associated with speech to text for the voice assistant.

    This is only relevant if the assistant uses a text-to-text language model. Any
    assistant using a model with native audio support (e.g.
    `fixie-ai/ultravox-v0_4`) will ignore this field.
    """

    user_response_timeout_ms: int
    """
    The number of milliseconds to wait for a user response before the voice
    assistant times out and check if the user is still there.
    """

    voice: str
    """The voice to be used by the voice assistant.

    Currently we support ElevenLabs, Telnyx and AWS voices.

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
      `ElevenLabs.BaseModel.John`). The `ModelId` part is optional. To use
      ElevenLabs, you must provide your ElevenLabs API key as an integration secret
      under `"voice_settings": {"api_key_ref": "<secret_id>"}`. See
      [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
      for details. Check
      [available voices](https://elevenlabs.io/docs/api-reference/get-voices).
    - **Telnyx:** Use `Telnyx.<model_id>.<voice_id>`
    """

    voice_settings: VoiceSettings
    """The settings associated with the voice selected"""


class MessageHistory(TypedDict, total=False):
    content: str
    """The content of the message"""

    role: Literal["assistant", "user"]
    """The role of the message sender"""


VoiceSettings: TypeAlias = Union[ElevenLabsVoiceSettingsParam, TelnyxVoiceSettingsParam, AwsVoiceSettingsParam]

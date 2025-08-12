# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Required, TypedDict

from .enabled_features import EnabledFeatures
from .assistant_tool_param import AssistantToolParam
from .voice_settings_param import VoiceSettingsParam
from .insight_settings_param import InsightSettingsParam
from .privacy_settings_param import PrivacySettingsParam
from .messaging_settings_param import MessagingSettingsParam
from .telephony_settings_param import TelephonySettingsParam
from .transcription_settings_param import TranscriptionSettingsParam

__all__ = ["AssistantCreateParams"]


class AssistantCreateParams(TypedDict, total=False):
    instructions: Required[str]
    """System instructions for the assistant.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    model: Required[str]
    """ID of the model to use.

    You can use the
    [Get models API](https://developers.telnyx.com/api/inference/inference-embedding/get-models-public-models-get)
    to see all of your available models,
    """

    name: Required[str]

    description: str

    dynamic_variables: Dict[str, object]
    """Map of dynamic variables and their default values"""

    dynamic_variables_webhook_url: str
    """
    If the dynamic_variables_webhook_url is set for the assistant, we will send a
    request at the start of the conversation. See our
    [guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    for more information.
    """

    enabled_features: List[EnabledFeatures]

    greeting: str
    """Text that the assistant will use to start the conversation.

    This may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    insight_settings: InsightSettingsParam

    llm_api_key_ref: str
    """This is only needed when using third-party inference providers.

    The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your LLM provider's API key. Warning: Free plans are unlikely to
    work with this integration.
    """

    messaging_settings: MessagingSettingsParam

    privacy_settings: PrivacySettingsParam

    telephony_settings: TelephonySettingsParam

    tools: Iterable[AssistantToolParam]
    """The tools that the assistant can use.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    transcription: TranscriptionSettingsParam

    voice_settings: VoiceSettingsParam

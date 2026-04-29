# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr
from ..enabled_features import EnabledFeatures
from ..assistant_tool_param import AssistantToolParam
from ..voice_settings_param import VoiceSettingsParam
from ..widget_settings_param import WidgetSettingsParam
from ..insight_settings_param import InsightSettingsParam
from ..privacy_settings_param import PrivacySettingsParam
from ..observability_req_param import ObservabilityReqParam
from ..messaging_settings_param import MessagingSettingsParam
from ..telephony_settings_param import TelephonySettingsParam
from ..transcription_settings_param import TranscriptionSettingsParam

__all__ = [
    "VersionUpdateParams",
    "ExternalLlm",
    "FallbackConfig",
    "FallbackConfigExternalLlm",
    "PostConversationSettings",
]


class VersionUpdateParams(TypedDict, total=False):
    assistant_id: Required[str]

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

    external_llm: ExternalLlm

    fallback_config: FallbackConfig

    greeting: str
    """Text that the assistant will use to start the conversation.

    This may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
    Use an empty string to have the assistant wait for the user to speak first. Use
    the special value `<assistant-speaks-first-with-model-generated-message>` to
    have the assistant generate the greeting based on the system instructions.
    """

    insight_settings: InsightSettingsParam

    instructions: str
    """System instructions for the assistant.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    llm_api_key_ref: str
    """This is only needed when using third-party inference providers.

    The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    that refers to your LLM provider's API key. Warning: Free plans are unlikely to
    work with this integration.
    """

    messaging_settings: MessagingSettingsParam

    model: str
    """ID of the model to use.

    You can use the
    [Get models API](https://developers.telnyx.com/api-reference/chat/get-available-models)
    to see all of your available models,
    """

    name: str

    observability_settings: ObservabilityReqParam

    post_conversation_settings: PostConversationSettings
    """Configuration for post-conversation processing.

    When enabled, the assistant receives one additional LLM turn after the
    conversation ends, allowing it to execute tool calls such as logging to a CRM or
    sending a summary. The assistant can execute multiple parallel or sequential
    tools during this phase. Telephony-control tools (e.g. hangup, transfer) are
    unavailable post-conversation. Beta feature.
    """

    privacy_settings: PrivacySettingsParam

    telephony_settings: TelephonySettingsParam

    tool_ids: SequenceNotStr[str]

    tools: Iterable[AssistantToolParam]
    """The tools that the assistant can use.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    transcription: TranscriptionSettingsParam

    voice_settings: VoiceSettingsParam

    widget_settings: WidgetSettingsParam
    """Configuration settings for the assistant's web widget."""


class ExternalLlm(TypedDict, total=False):
    base_url: Required[str]
    """Base URL for the external LLM endpoint."""

    model: Required[str]
    """Model identifier to use with the external LLM endpoint."""

    authentication_method: Literal["token", "certificate"]
    """Authentication method used when connecting to the external LLM endpoint."""

    certificate_ref: str
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    forward_metadata: bool
    """
    When enabled, Telnyx forwards the assistant's dynamic variables to the external
    LLM endpoint. Defaults to false. The chat completion request includes a
    top-level `extra_metadata` object when dynamic variables are available. For
    example:
    `{"extra_metadata":{"customer_name":"Jane","account_id":"acct_789","telnyx_agent_target":"+13125550100","telnyx_end_user_target":"+13125550123"}}`.
    """

    llm_api_key_ref: str
    """Integration secret identifier for the external LLM API key."""

    token_retrieval_url: str
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """


class FallbackConfigExternalLlm(TypedDict, total=False):
    base_url: Required[str]
    """Base URL for the external LLM endpoint."""

    model: Required[str]
    """Model identifier to use with the external LLM endpoint."""

    authentication_method: Literal["token", "certificate"]
    """Authentication method used when connecting to the external LLM endpoint."""

    certificate_ref: str
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    forward_metadata: bool
    """
    When enabled, Telnyx forwards the assistant's dynamic variables to the external
    LLM endpoint. Defaults to false. The chat completion request includes a
    top-level `extra_metadata` object when dynamic variables are available. For
    example:
    `{"extra_metadata":{"customer_name":"Jane","account_id":"acct_789","telnyx_agent_target":"+13125550100","telnyx_end_user_target":"+13125550123"}}`.
    """

    llm_api_key_ref: str
    """Integration secret identifier for the external LLM API key."""

    token_retrieval_url: str
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """


class FallbackConfig(TypedDict, total=False):
    external_llm: FallbackConfigExternalLlm

    llm_api_key_ref: str
    """Integration secret identifier for the fallback model API key."""

    model: str
    """
    Fallback Telnyx-hosted model to use when the primary LLM provider is
    unavailable.
    """


class PostConversationSettings(TypedDict, total=False):
    """Configuration for post-conversation processing.

    When enabled, the assistant receives one additional LLM turn after the conversation ends, allowing it to execute tool calls such as logging to a CRM or sending a summary. The assistant can execute multiple parallel or sequential tools during this phase. Telephony-control tools (e.g. hangup, transfer) are unavailable post-conversation. Beta feature.
    """

    enabled: bool
    """Whether post-conversation processing is enabled.

    When true, the assistant will be invoked after the conversation ends to perform
    any final tool calls. Defaults to false.
    """

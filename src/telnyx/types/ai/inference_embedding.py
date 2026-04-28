# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .observability import Observability
from .assistant_tool import AssistantTool
from .voice_settings import VoiceSettings
from .import_metadata import ImportMetadata
from .widget_settings import WidgetSettings
from .enabled_features import EnabledFeatures
from .insight_settings import InsightSettings
from .privacy_settings import PrivacySettings
from .messaging_settings import MessagingSettings
from .telephony_settings import TelephonySettings
from .transcription_settings import TranscriptionSettings

__all__ = [
    "InferenceEmbedding",
    "ExternalLlm",
    "FallbackConfig",
    "FallbackConfigExternalLlm",
    "PostConversationSettings",
]


class ExternalLlm(BaseModel):
    base_url: str
    """Base URL for the external LLM endpoint."""

    model: str
    """Model identifier to use with the external LLM endpoint."""

    authentication_method: Optional[Literal["token", "certificate"]] = None
    """Authentication method used when connecting to the external LLM endpoint."""

    certificate_ref: Optional[str] = None
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    forward_metadata: Optional[bool] = None
    """
    When enabled, Telnyx forwards conversation metadata and dynamic variables to the
    external LLM endpoint. Defaults to false. The external endpoint receives the
    standard chat completions payload with top-level `metadata` and
    `dynamic_variables` objects when values are available. For example:
    `{"metadata":{"conversation_id":"conv_123","assistant_id":"assistant_456","call_control_id":"v3:abc123","telnyx_conversation_channel":"phone_call"},"dynamic_variables":{"customer_name":"Jane","account_id":"acct_789","telnyx_agent_target":"+13125550100","telnyx_end_user_target":"+13125550123"}}`.
    """

    llm_api_key_ref: Optional[str] = None
    """Integration secret identifier for the external LLM API key."""

    token_retrieval_url: Optional[str] = None
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """


class FallbackConfigExternalLlm(BaseModel):
    base_url: str
    """Base URL for the external LLM endpoint."""

    model: str
    """Model identifier to use with the external LLM endpoint."""

    authentication_method: Optional[Literal["token", "certificate"]] = None
    """Authentication method used when connecting to the external LLM endpoint."""

    certificate_ref: Optional[str] = None
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    forward_metadata: Optional[bool] = None
    """
    When enabled, Telnyx forwards conversation metadata and dynamic variables to the
    external LLM endpoint. Defaults to false. The external endpoint receives the
    standard chat completions payload with top-level `metadata` and
    `dynamic_variables` objects when values are available. For example:
    `{"metadata":{"conversation_id":"conv_123","assistant_id":"assistant_456","call_control_id":"v3:abc123","telnyx_conversation_channel":"phone_call"},"dynamic_variables":{"customer_name":"Jane","account_id":"acct_789","telnyx_agent_target":"+13125550100","telnyx_end_user_target":"+13125550123"}}`.
    """

    llm_api_key_ref: Optional[str] = None
    """Integration secret identifier for the external LLM API key."""

    token_retrieval_url: Optional[str] = None
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """


class FallbackConfig(BaseModel):
    external_llm: Optional[FallbackConfigExternalLlm] = None

    llm_api_key_ref: Optional[str] = None
    """Integration secret identifier for the fallback model API key."""

    model: Optional[str] = None
    """
    Fallback Telnyx-hosted model to use when the primary LLM provider is
    unavailable.
    """


class PostConversationSettings(BaseModel):
    """Configuration for post-conversation processing.

    When enabled, the assistant receives one additional LLM turn after the conversation ends, allowing it to execute tool calls such as logging to a CRM or sending a summary. The assistant can execute multiple parallel or sequential tools during this phase. Telephony-control tools (e.g. hangup, transfer) are unavailable post-conversation. Beta feature.
    """

    enabled: Optional[bool] = None
    """Whether post-conversation processing is enabled.

    When true, the assistant will be invoked after the conversation ends to perform
    any final tool calls. Defaults to false.
    """


class InferenceEmbedding(BaseModel):
    id: str

    created_at: datetime

    instructions: str
    """System instructions for the assistant.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    model: str
    """ID of the model to use.

    You can use the
    [Get models API](https://developers.telnyx.com/api-reference/chat/get-available-models)
    to see all of your available models,
    """

    name: str

    description: Optional[str] = None

    dynamic_variables: Optional[Dict[str, object]] = None
    """Map of dynamic variables and their values"""

    dynamic_variables_webhook_url: Optional[str] = None
    """
    If the dynamic_variables_webhook_url is set for the assistant, we will send a
    request at the start of the conversation. See our
    [guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    for more information.
    """

    enabled_features: Optional[List[EnabledFeatures]] = None

    external_llm: Optional[ExternalLlm] = None

    fallback_config: Optional[FallbackConfig] = None

    greeting: Optional[str] = None
    """Text that the assistant will use to start the conversation.

    This may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
    Use an empty string to have the assistant wait for the user to speak first. Use
    the special value `<assistant-speaks-first-with-model-generated-message>` to
    have the assistant generate the greeting based on the system instructions.
    """

    import_metadata: Optional[ImportMetadata] = None

    insight_settings: Optional[InsightSettings] = None

    llm_api_key_ref: Optional[str] = None
    """This is only needed when using third-party inference providers.

    The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    that refers to your LLM provider's API key. Warning: Free plans are unlikely to
    work with this integration.
    """

    messaging_settings: Optional[MessagingSettings] = None

    observability_settings: Optional[Observability] = None

    post_conversation_settings: Optional[PostConversationSettings] = None
    """Configuration for post-conversation processing.

    When enabled, the assistant receives one additional LLM turn after the
    conversation ends, allowing it to execute tool calls such as logging to a CRM or
    sending a summary. The assistant can execute multiple parallel or sequential
    tools during this phase. Telephony-control tools (e.g. hangup, transfer) are
    unavailable post-conversation. Beta feature.
    """

    privacy_settings: Optional[PrivacySettings] = None

    telephony_settings: Optional[TelephonySettings] = None

    tools: Optional[List[AssistantTool]] = None
    """The tools that the assistant can use.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    transcription: Optional[TranscriptionSettings] = None

    voice_settings: Optional[VoiceSettings] = None

    widget_settings: Optional[WidgetSettings] = None
    """Configuration settings for the assistant's web widget."""

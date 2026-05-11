# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from .external_llm import ExternalLlm
from .observability import Observability
from .assistant_tool import AssistantTool
from .voice_settings import VoiceSettings
from .fallback_config import FallbackConfig
from .import_metadata import ImportMetadata
from .widget_settings import WidgetSettings
from .enabled_features import EnabledFeatures
from .insight_settings import InsightSettings
from .privacy_settings import PrivacySettings
from .messaging_settings import MessagingSettings
from .telephony_settings import TelephonySettings
from .assistant_mcp_server import AssistantMcpServer
from .assistant_integration import AssistantIntegration
from .transcription_settings import TranscriptionSettings
from .post_conversation_settings import PostConversationSettings
from .inference_embedding_interruption_settings import InferenceEmbeddingInterruptionSettings

__all__ = ["InferenceEmbedding"]


class InferenceEmbedding(BaseModel):
    id: str

    created_at: datetime

    instructions: str
    """System instructions for the assistant.

    These may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    """

    model: str
    """ID of the model to use when `external_llm` is not set.

    You can use the
    [Get models API](https://developers.telnyx.com/api-reference/openai-chat/get-available-models-openai-compatible)
    to see available models. If `external_llm` is provided, the assistant uses
    `external_llm` instead of this field. If neither `model` nor `external_llm` is
    provided, Telnyx applies the default model.
    """

    name: str

    description: Optional[str] = None

    dynamic_variables: Optional[Dict[str, object]] = None
    """Map of dynamic variables and their values"""

    dynamic_variables_webhook_timeout_ms: Optional[int] = None
    """Timeout in milliseconds for the dynamic variables webhook.

    Must be between 1 and 10000 ms. If the webhook does not respond within this
    timeout, the call proceeds with default values. See the
    [dynamic variables guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
    """

    dynamic_variables_webhook_url: Optional[str] = None
    """
    If `dynamic_variables_webhook_url` is set, Telnyx sends a POST request to this
    URL at the start of the conversation to resolve dynamic variables. **Gotcha:**
    the webhook response must wrap variables under a top-level `dynamic_variables`
    object, e.g. `{"dynamic_variables": {"customer_name": "Jane"}}`. Returning a
    flat object will be ignored and variables will fall back to their defaults. See
    the
    [dynamic variables guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    for the full request/response format and timeout behavior.
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

    integrations: Optional[List[AssistantIntegration]] = None
    """Connected integrations attached to the assistant.

    The catalog of available integrations is at `/ai/integrations`; the user's
    connected integrations are at `/ai/integrations/connections`. Each item
    references a catalog integration by `integration_id`.
    """

    interruption_settings: Optional[InferenceEmbeddingInterruptionSettings] = None
    """
    Settings for interruptions and how the assistant decides the user has finished
    speaking. These timings are most relevant when using non turn-taking
    transcription models. For turn-taking models like `deepgram/flux`, end-of-turn
    behavior is controlled by the transcription end-of-turn settings under
    `transcription.settings` (`eot_threshold`, `eot_timeout_ms`,
    `eager_eot_threshold`).
    """

    llm_api_key_ref: Optional[str] = None
    """
    This is only needed when using third-party inference providers selected by
    `model`. The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    that refers to your LLM provider's API key. For bring-your-own endpoint
    authentication, use `external_llm.llm_api_key_ref` instead. Warning: Free plans
    are unlikely to work with this integration.
    """

    mcp_servers: Optional[List[AssistantMcpServer]] = None
    """MCP servers attached to the assistant.

    Create MCP servers with `/ai/mcp_servers`, then reference them by `id` here.
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

    related_mission_ids: Optional[List[str]] = None
    """IDs of missions related to this assistant."""

    tags: Optional[List[str]] = None
    """Tags associated with the assistant.

    Tags can also be managed with the assistant tag endpoints.
    """

    telephony_settings: Optional[TelephonySettings] = None

    tools: Optional[List[AssistantTool]] = None
    """Deprecated for new integrations.

    Inline tool definitions available to the assistant. Prefer `tool_ids` to attach
    shared tools created with the AI Tools endpoints.
    """

    transcription: Optional[TranscriptionSettings] = None

    version_created_at: Optional[datetime] = None
    """Timestamp when this assistant version was created."""

    version_id: Optional[str] = None
    """
    Identifier for the assistant version returned by version-aware assistant
    endpoints.
    """

    version_name: Optional[str] = None
    """Human-readable name for the assistant version."""

    voice_settings: Optional[VoiceSettings] = None

    widget_settings: Optional[WidgetSettings] = None
    """Configuration settings for the assistant's web widget."""

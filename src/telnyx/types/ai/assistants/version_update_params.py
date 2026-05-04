# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr
from ..enabled_features import EnabledFeatures
from ..assistant_tool_param import AssistantToolParam
from ..voice_settings_param import VoiceSettingsParam
from ..widget_settings_param import WidgetSettingsParam
from ..external_llm_req_param import ExternalLlmReqParam
from ..insight_settings_param import InsightSettingsParam
from ..privacy_settings_param import PrivacySettingsParam
from ..observability_req_param import ObservabilityReqParam
from ..messaging_settings_param import MessagingSettingsParam
from ..telephony_settings_param import TelephonySettingsParam
from ..fallback_config_req_param import FallbackConfigReqParam
from ..transcription_settings_param import TranscriptionSettingsParam
from ..post_conversation_settings_req_param import PostConversationSettingsReqParam

__all__ = [
    "VersionUpdateParams",
    "Integration",
    "InterruptionSettings",
    "InterruptionSettingsStartSpeakingPlan",
    "InterruptionSettingsStartSpeakingPlanTranscriptionEndpointingPlan",
    "McpServer",
]


class VersionUpdateParams(TypedDict, total=False):
    assistant_id: Required[str]

    description: str

    dynamic_variables: Dict[str, object]
    """Map of dynamic variables and their default values"""

    dynamic_variables_webhook_timeout_ms: int
    """Timeout in milliseconds for the dynamic variables webhook.

    Must be between 1 and 10000 ms. If the webhook does not respond within this
    timeout, the call proceeds with default values. See the
    [dynamic variables guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
    """

    dynamic_variables_webhook_url: str
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

    enabled_features: List[EnabledFeatures]

    external_llm: ExternalLlmReqParam

    fallback_config: FallbackConfigReqParam

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

    integrations: Iterable[Integration]
    """Connected integrations attached to the assistant.

    The catalog of available integrations is at `/ai/integrations`; the user's
    connected integrations are at `/ai/integrations/connections`. Each item
    references a catalog integration by `integration_id`.
    """

    interruption_settings: InterruptionSettings
    """
    Settings for interruptions and how the assistant decides the user has finished
    speaking. These timings are most relevant when using non turn-taking
    transcription models. For turn-taking models like `deepgram/flux`, end-of-turn
    behavior is controlled by the transcription end-of-turn settings under
    `transcription.settings` (`eot_threshold`, `eot_timeout_ms`,
    `eager_eot_threshold`).
    """

    llm_api_key_ref: str
    """
    This is only needed when using third-party inference providers selected by
    `model`. The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    that refers to your LLM provider's API key. For bring-your-own endpoint
    authentication, use `external_llm.llm_api_key_ref` instead. Warning: Free plans
    are unlikely to work with this integration.
    """

    mcp_servers: Iterable[McpServer]
    """MCP servers attached to the assistant.

    Create MCP servers with `/ai/mcp_servers`, then reference them by `id` here.
    """

    messaging_settings: MessagingSettingsParam

    model: str
    """ID of the model to use when `external_llm` is not set.

    You can use the
    [Get models API](https://developers.telnyx.com/api-reference/chat/get-available-models)
    to see available models. If `external_llm` is provided, the assistant uses
    `external_llm` instead of this field. If neither `model` nor `external_llm` is
    provided, Telnyx applies the default model.
    """

    name: str

    observability_settings: ObservabilityReqParam

    post_conversation_settings: PostConversationSettingsReqParam
    """Configuration for post-conversation processing.

    When enabled, the assistant receives one additional LLM turn after the
    conversation ends, allowing it to execute tool calls such as logging to a CRM or
    sending a summary. The assistant can execute multiple parallel or sequential
    tools during this phase. Telephony-control tools (e.g. hangup, transfer) are
    unavailable post-conversation. Beta feature.
    """

    privacy_settings: PrivacySettingsParam

    tags: SequenceNotStr[str]
    """Tags associated with the assistant.

    Tags can also be managed with the assistant tag endpoints.
    """

    telephony_settings: TelephonySettingsParam

    tool_ids: SequenceNotStr[str]
    """IDs of shared tools to attach to the assistant.

    New integrations should prefer `tool_ids` over inline `tools`.
    """

    tools: Iterable[AssistantToolParam]
    """Deprecated for new integrations.

    Inline tool definitions available to the assistant. Prefer `tool_ids` to attach
    shared tools created with the AI Tools endpoints.
    """

    transcription: TranscriptionSettingsParam

    version_name: str
    """Human-readable name for the assistant version."""

    voice_settings: VoiceSettingsParam

    widget_settings: WidgetSettingsParam
    """Configuration settings for the assistant's web widget."""


class Integration(TypedDict, total=False):
    """Reference to a connected integration attached to an assistant.

    Discover available integrations with `/ai/integrations` and connected integrations with `/ai/integrations/connections`.
    """

    integration_id: Required[str]
    """Catalog integration ID to attach.

    This is the `id` from the integrations catalog at `/ai/integrations` (the same
    value also appears as `integration_id` on entries returned by
    `/ai/integrations/connections`). It is **not** the connection-level `id` from
    `/ai/integrations/connections`.
    """

    allowed_list: SequenceNotStr[str]
    """Optional per-assistant allowlist of integration tool names.

    When omitted or empty, all tools allowed by the connected integration are
    available to the assistant.
    """


class InterruptionSettingsStartSpeakingPlanTranscriptionEndpointingPlan(TypedDict, total=False):
    """Endpointing thresholds used to decide when the user has finished speaking.

    Applies to non turn-taking transcription models. For `deepgram/flux`, use `transcription.settings.eot_threshold` / `eot_timeout_ms` / `eager_eot_threshold`.
    """

    on_no_punctuation_seconds: float
    """Seconds to wait after the transcript ends without punctuation."""

    on_number_seconds: float
    """Seconds to wait after the transcript ends with a number."""

    on_punctuation_seconds: float
    """Seconds to wait after the transcript ends with punctuation."""


class InterruptionSettingsStartSpeakingPlan(TypedDict, total=False):
    """Controls when the assistant starts speaking after the user stops.

    These thresholds primarily apply to non turn-taking transcription models. For turn-taking models like `deepgram/flux`, end-of-turn detection is driven by the transcription end-of-turn settings under `transcription.settings` instead.
    """

    transcription_endpointing_plan: InterruptionSettingsStartSpeakingPlanTranscriptionEndpointingPlan
    """Endpointing thresholds used to decide when the user has finished speaking.

    Applies to non turn-taking transcription models. For `deepgram/flux`, use
    `transcription.settings.eot_threshold` / `eot_timeout_ms` /
    `eager_eot_threshold`.
    """

    wait_seconds: float
    """Minimum seconds to wait before the assistant starts speaking."""


class InterruptionSettings(TypedDict, total=False):
    """
    Settings for interruptions and how the assistant decides the user has finished speaking. These timings are most relevant when using non turn-taking transcription models. For turn-taking models like `deepgram/flux`, end-of-turn behavior is controlled by the transcription end-of-turn settings under `transcription.settings` (`eot_threshold`, `eot_timeout_ms`, `eager_eot_threshold`).
    """

    enable: bool
    """Whether users can interrupt the assistant while it is speaking."""

    start_speaking_plan: InterruptionSettingsStartSpeakingPlan
    """Controls when the assistant starts speaking after the user stops.

    These thresholds primarily apply to non turn-taking transcription models. For
    turn-taking models like `deepgram/flux`, end-of-turn detection is driven by the
    transcription end-of-turn settings under `transcription.settings` instead.
    """


class McpServer(TypedDict, total=False):
    """Reference to an MCP server attached to an assistant.

    Create and manage MCP servers with the `/ai/mcp_servers` endpoints, then attach them to assistants by ID.
    """

    id: Required[str]
    """ID of the MCP server to attach.

    This must be the `id` of an MCP server returned by the `/ai/mcp_servers`
    endpoints.
    """

    allowed_tools: SequenceNotStr[str]
    """Optional per-assistant allowlist of MCP tool names.

    When omitted, the assistant uses the MCP server's configured `allowed_tools`.
    """

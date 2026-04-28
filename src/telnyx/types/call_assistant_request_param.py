# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .ai.hangup_tool_param import HangupToolParam
from .ai.webhook_tool_param import WebhookToolParam
from .ai.transfer_tool_param import TransferToolParam
from .shared_params.book_appointment_tool import BookAppointmentTool
from .shared_params.check_availability_tool import CheckAvailabilityTool
from .shared_params.call_control_retrieval_tool import CallControlRetrievalTool

__all__ = ["CallAssistantRequestParam", "ExternalLlm", "FallbackConfig", "FallbackConfigExternalLlm", "Tool"]


class ExternalLlm(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """External LLM configuration for bringing your own LLM endpoint."""

    authentication_method: Literal["token", "certificate"]
    """Authentication method used when connecting to the external LLM endpoint."""

    base_url: str
    """Base URL for the external LLM endpoint."""

    certificate_ref: str
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    forward_metadata: bool
    """
    When enabled, Telnyx forwards conversation metadata and dynamic variables to the
    external LLM endpoint. Defaults to false. The external endpoint receives the
    standard chat completions payload with top-level `metadata` and
    `dynamic_variables` objects when values are available. For example:
    `{"metadata":{"conversation_id":"conv_123","assistant_id":"assistant_456","call_control_id":"v3:abc123","telnyx_conversation_channel":"phone_call"},"dynamic_variables":{"customer_name":"Jane","account_id":"acct_789","telnyx_agent_target":"+13125550100","telnyx_end_user_target":"+13125550123"}}`.
    """

    llm_api_key_ref: str
    """Integration secret identifier for the external LLM API key."""

    model: str
    """Model identifier to use with the external LLM endpoint."""

    token_retrieval_url: str
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """


class FallbackConfigExternalLlm(TypedDict, total=False):
    """External LLM fallback configuration."""

    authentication_method: Literal["token", "certificate"]
    """Authentication method used when connecting to the external LLM endpoint."""

    base_url: str
    """Base URL for the external LLM endpoint."""

    certificate_ref: str
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    forward_metadata: bool
    """
    When enabled, Telnyx forwards conversation metadata and dynamic variables to the
    external LLM endpoint. Defaults to false. The external endpoint receives the
    standard chat completions payload with top-level `metadata` and
    `dynamic_variables` objects when values are available. For example:
    `{"metadata":{"conversation_id":"conv_123","assistant_id":"assistant_456","call_control_id":"v3:abc123","telnyx_conversation_channel":"phone_call"},"dynamic_variables":{"customer_name":"Jane","account_id":"acct_789","telnyx_agent_target":"+13125550100","telnyx_end_user_target":"+13125550123"}}`.
    """

    llm_api_key_ref: str
    """Integration secret identifier for the external LLM API key."""

    model: str
    """Model identifier to use with the external LLM endpoint."""

    token_retrieval_url: str
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """


class FallbackConfig(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Fallback LLM configuration used when the primary LLM provider is unavailable."""

    external_llm: FallbackConfigExternalLlm
    """External LLM fallback configuration."""

    llm_api_key_ref: str
    """Integration secret identifier for the fallback model API key."""

    model: str
    """
    Fallback Telnyx-hosted model to use when the primary LLM provider is
    unavailable.
    """


Tool: TypeAlias = Union[
    BookAppointmentTool,
    CheckAvailabilityTool,
    WebhookToolParam,
    HangupToolParam,
    TransferToolParam,
    CallControlRetrievalTool,
]


class CallAssistantRequestParam(TypedDict, total=False):
    """AI Assistant configuration.

    All fields except `id` are optional — the assistant's stored configuration will be used as fallback for any omitted fields.
    """

    id: Required[str]
    """The identifier of the AI assistant to use."""

    dynamic_variables: Dict[str, Union[str, float, bool]]
    """Map of dynamic variables and their default values.

    Dynamic variables can be referenced in instructions, greeting, and tool
    definitions using the `{{variable_name}}` syntax. Call-control-agent
    automatically merges in `telnyx_call_*` variables (telnyx_call_to,
    telnyx_call_from, telnyx_conversation_channel, telnyx_agent_target,
    telnyx_end_user_target, telnyx_call_caller_id_name) and custom header variables.
    """

    external_llm: ExternalLlm
    """External LLM configuration for bringing your own LLM endpoint."""

    fallback_config: FallbackConfig
    """Fallback LLM configuration used when the primary LLM provider is unavailable."""

    greeting: str
    """Initial greeting text spoken when the assistant starts.

    Can be plain text for any voice or SSML for `AWS.Polly.<voice_id>` voices. There
    is a 3,000 character limit.
    """

    instructions: str
    """System instructions for the voice assistant.

    Can be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).
    This will overwrite the instructions set in the assistant configuration.
    """

    llm_api_key_ref: str
    """Integration secret identifier for the LLM provider API key.

    Use this field to reference an
    [integration secret](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    containing your LLM provider API key. Supports any LLM provider (OpenAI,
    Anthropic, etc.).
    """

    mcp_servers: Iterable[Dict[str, object]]
    """
    MCP (Model Context Protocol) server configurations for extending the assistant's
    capabilities with external tools and data sources.
    """

    model: str
    """LLM model override for this call.

    If omitted, the assistant's configured model is used.
    """

    name: str
    """Assistant name override for this call."""

    observability_settings: Dict[str, object]
    """
    Observability configuration for the assistant session, including Langfuse
    integration for tracing and monitoring.
    """

    openai_api_key_ref: str
    """Deprecated — use `llm_api_key_ref` instead.

    Integration secret identifier for the OpenAI API key. This field is maintained
    for backward compatibility; `llm_api_key_ref` is the canonical field name and
    supports all LLM providers.
    """

    tools: Iterable[Tool]
    """
    Inline tool definitions available to the assistant (webhook, retrieval,
    transfer, hangup, etc.). Overrides the assistant's stored tools if provided.
    """

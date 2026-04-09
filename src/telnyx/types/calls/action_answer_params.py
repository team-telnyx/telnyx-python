# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..stream_codec import StreamCodec
from ..sip_header_param import SipHeaderParam
from ..ai.hangup_tool_param import HangupToolParam
from ..ai.webhook_tool_param import WebhookToolParam
from ..ai.transfer_tool_param import TransferToolParam
from ..custom_sip_header_param import CustomSipHeaderParam
from ..sound_modifications_param import SoundModificationsParam
from ..stream_bidirectional_mode import StreamBidirectionalMode
from ..stream_bidirectional_codec import StreamBidirectionalCodec
from ..stream_bidirectional_target_legs import StreamBidirectionalTargetLegs
from .transcription_start_request_param import TranscriptionStartRequestParam

__all__ = [
    "ActionAnswerParams",
    "Assistant",
    "AssistantTool",
    "AssistantToolBookAppointmentTool",
    "AssistantToolBookAppointmentToolBookAppointment",
    "AssistantToolCheckAvailabilityTool",
    "AssistantToolCheckAvailabilityToolCheckAvailability",
    "AssistantToolCallControlRetrievalTool",
    "AssistantToolCallControlRetrievalToolRetrieval",
    "WebhookRetriesPolicies",
]


class ActionAnswerParams(TypedDict, total=False):
    assistant: Assistant
    """AI Assistant configuration.

    All fields except `id` are optional — the assistant's stored configuration will
    be used as fallback for any omitted fields.
    """

    billing_group_id: str
    """Use this field to set the Billing Group ID for the call.

    Must be a valid and existing Billing Group ID.
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

    custom_headers: Iterable[CustomSipHeaderParam]
    """Custom headers to be added to the SIP INVITE response."""

    preferred_codecs: Literal["G722,PCMU,PCMA,G729,OPUS,VP8,H264"]
    """
    The list of comma-separated codecs in a preferred order for the forked media to
    be received.
    """

    record: Literal["record-from-answer"]
    """Start recording automatically after an event. Disabled by default."""

    record_channels: Literal["single", "dual"]
    """
    Defines which channel should be recorded ('single' or 'dual') when `record` is
    specified.
    """

    record_custom_file_name: str
    """The custom recording file name to be used instead of the default `call_leg_id`.

    Telnyx will still add a Unix timestamp suffix.
    """

    record_format: Literal["wav", "mp3"]
    """
    Defines the format of the recording ('wav' or 'mp3') when `record` is specified.
    """

    record_max_length: int
    """
    Defines the maximum length for the recording in seconds when `record` is
    specified. The minimum value is 0. The maximum value is 43200. The default value
    is 0 (infinite).
    """

    record_timeout_secs: int
    """
    The number of seconds that Telnyx will wait for the recording to be stopped if
    silence is detected when `record` is specified. The timer only starts when the
    speech is detected. Please note that call transcription is used to detect
    silence and the related charge will be applied. The minimum value is 0. The
    default value is 0 (infinite).
    """

    record_track: Literal["both", "inbound", "outbound"]
    """The audio track to be recorded.

    Can be either `both`, `inbound` or `outbound`. If only single track is specified
    (`inbound`, `outbound`), `channels` configuration is ignored and it will be
    recorded as mono (single channel).
    """

    record_trim: Literal["trim-silence"]
    """
    When set to `trim-silence`, silence will be removed from the beginning and end
    of the recording.
    """

    send_silence_when_idle: bool
    """Generate silence RTP packets when no transmission available."""

    sip_headers: Iterable[SipHeaderParam]
    """SIP headers to be added to the SIP INVITE response.

    Currently only User-to-User header is supported.
    """

    sound_modifications: SoundModificationsParam
    """Use this field to modify sound effects, for example adjust the pitch."""

    stream_bidirectional_codec: StreamBidirectionalCodec
    """Indicates codec for bidirectional streaming RTP payloads.

    Used only with stream_bidirectional_mode=rtp. Case sensitive.
    """

    stream_bidirectional_mode: StreamBidirectionalMode
    """Configures method of bidirectional streaming (mp3, rtp)."""

    stream_bidirectional_target_legs: StreamBidirectionalTargetLegs
    """Specifies which call legs should receive the bidirectional stream audio."""

    stream_codec: StreamCodec
    """Specifies the codec to be used for the streamed audio.

    When set to 'default' or when transcoding is not possible, the codec from the
    call will be used.
    """

    stream_track: Literal["inbound_track", "outbound_track", "both_tracks"]
    """Specifies which track should be streamed."""

    stream_url: str
    """The destination WebSocket address where the stream is going to be delivered."""

    transcription: bool
    """Enable transcription upon call answer. The default value is false."""

    transcription_config: TranscriptionStartRequestParam

    webhook_retries_policies: Dict[str, WebhookRetriesPolicies]
    """A map of event types to retry policies.

    Each retry policy contains an array of `retries_ms` specifying the delays
    between retry attempts in milliseconds. Maximum 5 retries, total delay cannot
    exceed 60 seconds.
    """

    webhook_url: str
    """
    Use this field to override the URL for which Telnyx will send subsequent
    webhooks to for this call.
    """

    webhook_url_method: Literal["POST", "GET"]
    """HTTP request type used for `webhook_url`."""

    webhook_urls: Dict[str, str]
    """A map of event types to webhook URLs.

    When an event of the specified type occurs, the webhook URL associated with that
    event type will be called instead of `webhook_url`. Events not mapped here will
    use the default `webhook_url`.
    """

    webhook_urls_method: Literal["POST", "GET"]
    """HTTP request method to invoke `webhook_urls`."""


class AssistantToolBookAppointmentToolBookAppointment(TypedDict, total=False):
    api_key_ref: Required[str]
    """Reference to an integration secret that contains your Cal.com API key.

    You would pass the `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your Cal.com API key.
    """

    event_type_id: Required[int]
    """Event Type ID for which slots are being fetched.

    [cal.com](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#body-event-type-id)
    """

    attendee_name: str
    """
    The name of the attendee
    [cal.com](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#body-attendee-name).
    If not provided, the assistant will ask for the attendee's name.
    """

    attendee_timezone: str
    """
    The timezone of the attendee
    [cal.com](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#body-attendee-timezone).
    If not provided, the assistant will ask for the attendee's timezone.
    """


class AssistantToolBookAppointmentTool(TypedDict, total=False):
    book_appointment: Required[AssistantToolBookAppointmentToolBookAppointment]

    type: Required[Literal["book_appointment"]]


class AssistantToolCheckAvailabilityToolCheckAvailability(TypedDict, total=False):
    api_key_ref: Required[str]
    """Reference to an integration secret that contains your Cal.com API key.

    You would pass the `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your Cal.com API key.
    """

    event_type_id: Required[int]
    """Event Type ID for which slots are being fetched.

    [cal.com](https://cal.com/docs/api-reference/v2/slots/get-available-slots#parameter-event-type-id)
    """


class AssistantToolCheckAvailabilityTool(TypedDict, total=False):
    check_availability: Required[AssistantToolCheckAvailabilityToolCheckAvailability]

    type: Required[Literal["check_availability"]]


class AssistantToolCallControlRetrievalToolRetrieval(TypedDict, total=False):
    bucket_ids: Required[SequenceNotStr[str]]

    max_num_results: int
    """The maximum number of results to retrieve as context for the language model."""


class AssistantToolCallControlRetrievalTool(TypedDict, total=False):
    retrieval: Required[AssistantToolCallControlRetrievalToolRetrieval]

    type: Required[Literal["retrieval"]]


AssistantTool: TypeAlias = Union[
    AssistantToolBookAppointmentTool,
    AssistantToolCheckAvailabilityTool,
    WebhookToolParam,
    HangupToolParam,
    TransferToolParam,
    AssistantToolCallControlRetrievalTool,
]


class Assistant(TypedDict, total=False):
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

    external_llm: object
    """External LLM configuration for bringing your own LLM endpoint."""

    fallback_config: object
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

    mcp_servers: Iterable[object]
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

    observability_settings: object
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

    tools: Iterable[AssistantTool]
    """
    Inline tool definitions available to the assistant (webhook, retrieval,
    transfer, hangup, etc.). Overrides the assistant's stored tools if provided.
    """


class WebhookRetriesPolicies(TypedDict, total=False):
    retries_ms: Iterable[int]
    """Array of delays in milliseconds between retry attempts.

    Total sum cannot exceed 60000ms.
    """

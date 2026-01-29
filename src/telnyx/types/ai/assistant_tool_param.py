# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .hangup_tool_param import HangupToolParam
from .retrieval_tool_param import RetrievalToolParam

__all__ = [
    "AssistantToolParam",
    "Webhook",
    "WebhookWebhook",
    "WebhookWebhookBodyParameters",
    "WebhookWebhookHeader",
    "WebhookWebhookPathParameters",
    "WebhookWebhookQueryParameters",
    "Handoff",
    "HandoffHandoff",
    "HandoffHandoffAIAssistant",
    "Transfer",
    "TransferTransfer",
    "TransferTransferTarget",
    "TransferTransferCustomHeader",
    "Refer",
    "ReferRefer",
    "ReferReferTarget",
    "ReferReferCustomHeader",
    "ReferReferSipHeader",
    "SendDtmf",
    "SendMessage",
]


class WebhookWebhookBodyParameters(TypedDict, total=False):
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Dict[str, object]
    """The properties of the body parameters."""

    required: SequenceNotStr[str]
    """The required properties of the body parameters."""

    type: Literal["object"]


class WebhookWebhookHeader(TypedDict, total=False):
    name: str

    value: str
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `Bearer {{#integration_secret}}test-secret{{/integration_secret}}` to pass the
    value of the integration secret as the bearer token.
    [Telnyx signature headers](https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks)
    will be automatically added to the request.
    """


class WebhookWebhookPathParameters(TypedDict, total=False):
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the URL contains a placeholder for a value. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Dict[str, object]
    """The properties of the path parameters."""

    required: SequenceNotStr[str]
    """The required properties of the path parameters."""

    type: Literal["object"]


class WebhookWebhookQueryParameters(TypedDict, total=False):
    """The query parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the query of the request. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Dict[str, object]
    """The properties of the query parameters."""

    required: SequenceNotStr[str]
    """The required properties of the query parameters."""

    type: Literal["object"]


_WebhookWebhookReservedKeywords = TypedDict(
    "_WebhookWebhookReservedKeywords",
    {
        "async": bool,
    },
    total=False,
)


class WebhookWebhook(_WebhookWebhookReservedKeywords, total=False):
    description: Required[str]
    """The description of the tool."""

    name: Required[str]
    """The name of the tool."""

    url: Required[str]
    """The URL of the external tool to be called.

    This URL is going to be used by the assistant. The URL can be templated like:
    `https://example.com/api/v1/{id}`, where `{id}` is a placeholder for a value
    that will be provided by the assistant if `path_parameters` are provided with
    the `id` attribute.
    """

    body_parameters: WebhookWebhookBodyParameters
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    headers: Iterable[WebhookWebhookHeader]
    """The headers to be sent to the external tool."""

    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"]
    """The HTTP method to be used when calling the external tool."""

    path_parameters: WebhookWebhookPathParameters
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the
    URL contains a placeholder for a value. See the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema) for
    documentation about the format
    """

    query_parameters: WebhookWebhookQueryParameters
    """The query parameters the webhook tool accepts, described as a JSON Schema
    object.

    These parameters will be passed to the webhook as the query of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    timeout_ms: int
    """The maximum number of milliseconds to wait for the webhook to respond.

    Only applicable when async is false.
    """


class Webhook(TypedDict, total=False):
    type: Required[Literal["webhook"]]

    webhook: Required[WebhookWebhook]


class HandoffHandoffAIAssistant(TypedDict, total=False):
    id: Required[str]
    """The ID of the assistant to hand off to."""

    name: Required[str]
    """Helpful name for giving context on when to handoff to the assistant."""


class HandoffHandoff(TypedDict, total=False):
    ai_assistants: Required[Iterable[HandoffHandoffAIAssistant]]
    """List of possible assistants that can receive a handoff."""

    voice_mode: Literal["unified", "distinct"]
    """
    With the unified voice mode all assistants share the same voice, making the
    handoff transparent to the user. With the distinct voice mode all assistants
    retain their voice configuration, providing the experience of a conference call
    with a team of assistants.
    """


class Handoff(TypedDict, total=False):
    """
    The handoff tool allows the assistant to hand off control of the conversation to another AI assistant. By default, this will happen transparently to the end user.
    """

    handoff: Required[HandoffHandoff]

    type: Required[Literal["handoff"]]


class TransferTransferTarget(TypedDict, total=False):
    name: str
    """The name of the target."""

    to: str
    """The destination number or SIP URI of the call."""


class TransferTransferCustomHeader(TypedDict, total=False):
    name: str

    value: str
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


_TransferTransferReservedKeywords = TypedDict(
    "_TransferTransferReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class TransferTransfer(_TransferTransferReservedKeywords, total=False):
    targets: Required[Iterable[TransferTransferTarget]]
    """The different possible targets of the transfer.

    The assistant will be able to choose one of the targets to transfer the call to.
    """

    custom_headers: Iterable[TransferTransferCustomHeader]
    """Custom headers to be added to the SIP INVITE for the transfer command."""

    warm_transfer_instructions: str
    """
    Natural language instructions for your agent for how to provide context for the
    transfer recipient.
    """


class Transfer(TypedDict, total=False):
    transfer: Required[TransferTransfer]

    type: Required[Literal["transfer"]]


class ReferReferTarget(TypedDict, total=False):
    name: Required[str]
    """The name of the target."""

    sip_address: Required[str]
    """The SIP URI to which the call will be referred."""

    sip_auth_password: str
    """SIP Authentication password used for SIP challenges."""

    sip_auth_username: str
    """SIP Authentication username used for SIP challenges."""


class ReferReferCustomHeader(TypedDict, total=False):
    name: str

    value: str
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class ReferReferSipHeader(TypedDict, total=False):
    name: Literal["User-to-User", "Diversion"]

    value: str
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class ReferRefer(TypedDict, total=False):
    targets: Required[Iterable[ReferReferTarget]]
    """The different possible targets of the SIP refer.

    The assistant will be able to choose one of the targets to refer the call to.
    """

    custom_headers: Iterable[ReferReferCustomHeader]
    """Custom headers to be added to the SIP REFER."""

    sip_headers: Iterable[ReferReferSipHeader]
    """SIP headers to be added to the SIP REFER.

    Currently only User-to-User and Diversion headers are supported.
    """


class Refer(TypedDict, total=False):
    refer: Required[ReferRefer]

    type: Required[Literal["refer"]]


class SendDtmf(TypedDict, total=False):
    send_dtmf: Required[Dict[str, object]]

    type: Required[Literal["send_dtmf"]]


class SendMessage(TypedDict, total=False):
    """
    The send_message tool allows the assistant to send SMS or MMS messages to the end user. The 'to' and 'from' addresses are automatically determined from the conversation context, and the message text is generated by the assistant.
    """

    send_message: Required[Dict[str, object]]

    type: Required[Literal["send_message"]]


AssistantToolParam: TypeAlias = Union[
    Webhook, RetrievalToolParam, Handoff, HangupToolParam, Transfer, Refer, SendDtmf, SendMessage
]

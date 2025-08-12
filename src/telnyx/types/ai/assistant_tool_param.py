# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .bucket_ids_param import BucketIDsParam

__all__ = [
    "AssistantToolParam",
    "WebhookTool",
    "WebhookToolWebhook",
    "WebhookToolWebhookBodyParameters",
    "WebhookToolWebhookHeader",
    "WebhookToolWebhookPathParameters",
    "WebhookToolWebhookQueryParameters",
    "RetrievalTool",
    "HandoffTool",
    "HandoffToolHandoff",
    "HandoffToolHandoffAIAssistant",
    "HangupTool",
    "HangupToolHangup",
    "TransferTool",
    "TransferToolTransfer",
    "TransferToolTransferTarget",
    "TransferToolTransferCustomHeader",
    "SipReferTool",
    "SipReferToolRefer",
    "SipReferToolReferTarget",
    "SipReferToolReferCustomHeader",
    "SipReferToolReferSipHeader",
    "DtmfTool",
]


class WebhookToolWebhookBodyParameters(TypedDict, total=False):
    properties: Dict[str, object]
    """The properties of the body parameters."""

    required: List[str]
    """The required properties of the body parameters."""

    type: Literal["object"]


class WebhookToolWebhookHeader(TypedDict, total=False):
    name: str

    value: str
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `Bearer {{#integration_secret}}test-secret{{/integration_secret}}` to pass the
    value of the integration secret as the bearer token.
    """


class WebhookToolWebhookPathParameters(TypedDict, total=False):
    properties: Dict[str, object]
    """The properties of the path parameters."""

    required: List[str]
    """The required properties of the path parameters."""

    type: Literal["object"]


class WebhookToolWebhookQueryParameters(TypedDict, total=False):
    properties: Dict[str, object]
    """The properties of the query parameters."""

    required: List[str]
    """The required properties of the query parameters."""

    type: Literal["object"]


class WebhookToolWebhook(TypedDict, total=False):
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

    body_parameters: WebhookToolWebhookBodyParameters
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    headers: Iterable[WebhookToolWebhookHeader]
    """The headers to be sent to the external tool."""

    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"]
    """The HTTP method to be used when calling the external tool."""

    path_parameters: WebhookToolWebhookPathParameters
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the
    URL contains a placeholder for a value. See the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema) for
    documentation about the format
    """

    query_parameters: WebhookToolWebhookQueryParameters
    """The query parameters the webhook tool accepts, described as a JSON Schema
    object.

    These parameters will be passed to the webhook as the query of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """


class WebhookTool(TypedDict, total=False):
    type: Required[Literal["webhook"]]

    webhook: Required[WebhookToolWebhook]


class RetrievalTool(TypedDict, total=False):
    retrieval: Required[BucketIDsParam]

    type: Required[Literal["retrieval"]]


class HandoffToolHandoffAIAssistant(TypedDict, total=False):
    id: Required[str]
    """The ID of the assistant to hand off to."""

    name: Required[str]
    """Helpful name for giving context on when to handoff to the assistant."""


class HandoffToolHandoff(TypedDict, total=False):
    ai_assistants: Required[Iterable[HandoffToolHandoffAIAssistant]]
    """List of possible assistants that can receive a handoff."""

    voice_mode: Literal["unified", "distinct"]
    """
    With the unified voice mode all assistants share the same voice, making the
    handoff transparent to the user. With the distinct voice mode all assistants
    retain their voice configuration, providing the experience of a conference call
    with a team of assistants.
    """


class HandoffTool(TypedDict, total=False):
    handoff: Required[HandoffToolHandoff]

    type: Required[Literal["handoff"]]


class HangupToolHangup(TypedDict, total=False):
    description: str
    """The description of the function that will be passed to the assistant."""


class HangupTool(TypedDict, total=False):
    hangup: Required[HangupToolHangup]

    type: Required[Literal["hangup"]]


class TransferToolTransferTarget(TypedDict, total=False):
    name: str
    """The name of the target."""

    to: str
    """The destination number or SIP URI of the call."""


class TransferToolTransferCustomHeader(TypedDict, total=False):
    name: str

    value: str
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


_TransferToolTransferReservedKeywords = TypedDict(
    "_TransferToolTransferReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class TransferToolTransfer(_TransferToolTransferReservedKeywords, total=False):
    targets: Required[Iterable[TransferToolTransferTarget]]
    """The different possible targets of the transfer.

    The assistant will be able to choose one of the targets to transfer the call to.
    """

    custom_headers: Iterable[TransferToolTransferCustomHeader]
    """Custom headers to be added to the SIP INVITE for the transfer command."""


class TransferTool(TypedDict, total=False):
    transfer: Required[TransferToolTransfer]

    type: Required[Literal["transfer"]]


class SipReferToolReferTarget(TypedDict, total=False):
    name: Required[str]
    """The name of the target."""

    sip_address: Required[str]
    """The SIP URI to which the call will be referred."""

    sip_auth_password: str
    """SIP Authentication password used for SIP challenges."""

    sip_auth_username: str
    """SIP Authentication username used for SIP challenges."""


class SipReferToolReferCustomHeader(TypedDict, total=False):
    name: str

    value: str
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class SipReferToolReferSipHeader(TypedDict, total=False):
    name: Literal["User-to-User", "Diversion"]

    value: str
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class SipReferToolRefer(TypedDict, total=False):
    targets: Required[Iterable[SipReferToolReferTarget]]
    """The different possible targets of the SIP refer.

    The assistant will be able to choose one of the targets to refer the call to.
    """

    custom_headers: Iterable[SipReferToolReferCustomHeader]
    """Custom headers to be added to the SIP REFER."""

    sip_headers: Iterable[SipReferToolReferSipHeader]
    """SIP headers to be added to the SIP REFER.

    Currently only User-to-User and Diversion headers are supported.
    """


class SipReferTool(TypedDict, total=False):
    refer: Required[SipReferToolRefer]

    type: Required[Literal["refer"]]


class DtmfTool(TypedDict, total=False):
    send_dtmf: Required[Dict[str, object]]

    type: Required[Literal["send_dtmf"]]


AssistantToolParam: TypeAlias = Union[
    WebhookTool, RetrievalTool, HandoffTool, HangupTool, TransferTool, SipReferTool, DtmfTool
]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .hangup_tool import HangupTool
from .retrieval_tool import RetrievalTool

__all__ = [
    "AssistantTool",
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


class WebhookWebhookBodyParameters(BaseModel):
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Optional[Dict[str, object]] = None
    """The properties of the body parameters."""

    required: Optional[List[str]] = None
    """The required properties of the body parameters."""

    type: Optional[Literal["object"]] = None


class WebhookWebhookHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `Bearer {{#integration_secret}}test-secret{{/integration_secret}}` to pass the
    value of the integration secret as the bearer token.
    [Telnyx signature headers](https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks)
    will be automatically added to the request.
    """


class WebhookWebhookPathParameters(BaseModel):
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the URL contains a placeholder for a value. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Optional[Dict[str, object]] = None
    """The properties of the path parameters."""

    required: Optional[List[str]] = None
    """The required properties of the path parameters."""

    type: Optional[Literal["object"]] = None


class WebhookWebhookQueryParameters(BaseModel):
    """The query parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the query of the request. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Optional[Dict[str, object]] = None
    """The properties of the query parameters."""

    required: Optional[List[str]] = None
    """The required properties of the query parameters."""

    type: Optional[Literal["object"]] = None


class WebhookWebhook(BaseModel):
    description: str
    """The description of the tool."""

    name: str
    """The name of the tool."""

    url: str
    """The URL of the external tool to be called.

    This URL is going to be used by the assistant. The URL can be templated like:
    `https://example.com/api/v1/{id}`, where `{id}` is a placeholder for a value
    that will be provided by the assistant if `path_parameters` are provided with
    the `id` attribute.
    """

    async_: Optional[bool] = FieldInfo(alias="async", default=None)
    """
    If async, the assistant will move forward without waiting for your server to
    respond.
    """

    body_parameters: Optional[WebhookWebhookBodyParameters] = None
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    headers: Optional[List[WebhookWebhookHeader]] = None
    """The headers to be sent to the external tool."""

    method: Optional[Literal["GET", "POST", "PUT", "DELETE", "PATCH"]] = None
    """The HTTP method to be used when calling the external tool."""

    path_parameters: Optional[WebhookWebhookPathParameters] = None
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the
    URL contains a placeholder for a value. See the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema) for
    documentation about the format
    """

    query_parameters: Optional[WebhookWebhookQueryParameters] = None
    """The query parameters the webhook tool accepts, described as a JSON Schema
    object.

    These parameters will be passed to the webhook as the query of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    timeout_ms: Optional[int] = None
    """The maximum number of milliseconds to wait for the webhook to respond.

    Only applicable when async is false.
    """


class Webhook(BaseModel):
    type: Literal["webhook"]

    webhook: WebhookWebhook


class HandoffHandoffAIAssistant(BaseModel):
    id: str
    """The ID of the assistant to hand off to."""

    name: str
    """Helpful name for giving context on when to handoff to the assistant."""


class HandoffHandoff(BaseModel):
    ai_assistants: List[HandoffHandoffAIAssistant]
    """List of possible assistants that can receive a handoff."""

    voice_mode: Optional[Literal["unified", "distinct"]] = None
    """
    With the unified voice mode all assistants share the same voice, making the
    handoff transparent to the user. With the distinct voice mode all assistants
    retain their voice configuration, providing the experience of a conference call
    with a team of assistants.
    """


class Handoff(BaseModel):
    """
    The handoff tool allows the assistant to hand off control of the conversation to another AI assistant. By default, this will happen transparently to the end user.
    """

    handoff: HandoffHandoff

    type: Literal["handoff"]


class TransferTransferTarget(BaseModel):
    name: Optional[str] = None
    """The name of the target."""

    to: Optional[str] = None
    """The destination number or SIP URI of the call."""


class TransferTransferCustomHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class TransferTransfer(BaseModel):
    from_: str = FieldInfo(alias="from")
    """Number or SIP URI placing the call."""

    targets: List[TransferTransferTarget]
    """The different possible targets of the transfer.

    The assistant will be able to choose one of the targets to transfer the call to.
    """

    custom_headers: Optional[List[TransferTransferCustomHeader]] = None
    """Custom headers to be added to the SIP INVITE for the transfer command."""

    warm_transfer_instructions: Optional[str] = None
    """
    Natural language instructions for your agent for how to provide context for the
    transfer recipient.
    """


class Transfer(BaseModel):
    transfer: TransferTransfer

    type: Literal["transfer"]


class ReferReferTarget(BaseModel):
    name: str
    """The name of the target."""

    sip_address: str
    """The SIP URI to which the call will be referred."""

    sip_auth_password: Optional[str] = None
    """SIP Authentication password used for SIP challenges."""

    sip_auth_username: Optional[str] = None
    """SIP Authentication username used for SIP challenges."""


class ReferReferCustomHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class ReferReferSipHeader(BaseModel):
    name: Optional[Literal["User-to-User", "Diversion"]] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class ReferRefer(BaseModel):
    targets: List[ReferReferTarget]
    """The different possible targets of the SIP refer.

    The assistant will be able to choose one of the targets to refer the call to.
    """

    custom_headers: Optional[List[ReferReferCustomHeader]] = None
    """Custom headers to be added to the SIP REFER."""

    sip_headers: Optional[List[ReferReferSipHeader]] = None
    """SIP headers to be added to the SIP REFER.

    Currently only User-to-User and Diversion headers are supported.
    """


class Refer(BaseModel):
    refer: ReferRefer

    type: Literal["refer"]


class SendDtmf(BaseModel):
    send_dtmf: Dict[str, object]

    type: Literal["send_dtmf"]


class SendMessage(BaseModel):
    """
    The send_message tool allows the assistant to send SMS or MMS messages to the end user. The 'to' and 'from' addresses are automatically determined from the conversation context, and the message text is generated by the assistant.
    """

    send_message: Dict[str, object]

    type: Literal["send_message"]


AssistantTool: TypeAlias = Annotated[
    Union[Webhook, RetrievalTool, Handoff, HangupTool, Transfer, Refer, SendDtmf, SendMessage],
    PropertyInfo(discriminator="type"),
]

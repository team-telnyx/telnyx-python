# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .bucket_ids import BucketIDs

__all__ = [
    "AssistantTool",
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


class WebhookToolWebhookBodyParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None
    """The properties of the body parameters."""

    required: Optional[List[str]] = None
    """The required properties of the body parameters."""

    type: Optional[Literal["object"]] = None


class WebhookToolWebhookHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `Bearer {{#integration_secret}}test-secret{{/integration_secret}}` to pass the
    value of the integration secret as the bearer token.
    """


class WebhookToolWebhookPathParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None
    """The properties of the path parameters."""

    required: Optional[List[str]] = None
    """The required properties of the path parameters."""

    type: Optional[Literal["object"]] = None


class WebhookToolWebhookQueryParameters(BaseModel):
    properties: Optional[Dict[str, object]] = None
    """The properties of the query parameters."""

    required: Optional[List[str]] = None
    """The required properties of the query parameters."""

    type: Optional[Literal["object"]] = None


class WebhookToolWebhook(BaseModel):
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

    body_parameters: Optional[WebhookToolWebhookBodyParameters] = None
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    headers: Optional[List[WebhookToolWebhookHeader]] = None
    """The headers to be sent to the external tool."""

    method: Optional[Literal["GET", "POST", "PUT", "DELETE", "PATCH"]] = None
    """The HTTP method to be used when calling the external tool."""

    path_parameters: Optional[WebhookToolWebhookPathParameters] = None
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the
    URL contains a placeholder for a value. See the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema) for
    documentation about the format
    """

    query_parameters: Optional[WebhookToolWebhookQueryParameters] = None
    """The query parameters the webhook tool accepts, described as a JSON Schema
    object.

    These parameters will be passed to the webhook as the query of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """


class WebhookTool(BaseModel):
    type: Literal["webhook"]

    webhook: WebhookToolWebhook


class RetrievalTool(BaseModel):
    retrieval: BucketIDs

    type: Literal["retrieval"]


class HandoffToolHandoffAIAssistant(BaseModel):
    id: str
    """The ID of the assistant to hand off to."""

    name: str
    """Helpful name for giving context on when to handoff to the assistant."""


class HandoffToolHandoff(BaseModel):
    ai_assistants: List[HandoffToolHandoffAIAssistant]
    """List of possible assistants that can receive a handoff."""

    voice_mode: Optional[Literal["unified", "distinct"]] = None
    """
    With the unified voice mode all assistants share the same voice, making the
    handoff transparent to the user. With the distinct voice mode all assistants
    retain their voice configuration, providing the experience of a conference call
    with a team of assistants.
    """


class HandoffTool(BaseModel):
    handoff: HandoffToolHandoff

    type: Literal["handoff"]


class HangupToolHangup(BaseModel):
    description: Optional[str] = None
    """The description of the function that will be passed to the assistant."""


class HangupTool(BaseModel):
    hangup: HangupToolHangup

    type: Literal["hangup"]


class TransferToolTransferTarget(BaseModel):
    name: Optional[str] = None
    """The name of the target."""

    to: Optional[str] = None
    """The destination number or SIP URI of the call."""


class TransferToolTransferCustomHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class TransferToolTransfer(BaseModel):
    from_: str = FieldInfo(alias="from")
    """Number or SIP URI placing the call."""

    targets: List[TransferToolTransferTarget]
    """The different possible targets of the transfer.

    The assistant will be able to choose one of the targets to transfer the call to.
    """

    custom_headers: Optional[List[TransferToolTransferCustomHeader]] = None
    """Custom headers to be added to the SIP INVITE for the transfer command."""


class TransferTool(BaseModel):
    transfer: TransferToolTransfer

    type: Literal["transfer"]


class SipReferToolReferTarget(BaseModel):
    name: str
    """The name of the target."""

    sip_address: str
    """The SIP URI to which the call will be referred."""

    sip_auth_password: Optional[str] = None
    """SIP Authentication password used for SIP challenges."""

    sip_auth_username: Optional[str] = None
    """SIP Authentication username used for SIP challenges."""


class SipReferToolReferCustomHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class SipReferToolReferSipHeader(BaseModel):
    name: Optional[Literal["User-to-User", "Diversion"]] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class SipReferToolRefer(BaseModel):
    targets: List[SipReferToolReferTarget]
    """The different possible targets of the SIP refer.

    The assistant will be able to choose one of the targets to refer the call to.
    """

    custom_headers: Optional[List[SipReferToolReferCustomHeader]] = None
    """Custom headers to be added to the SIP REFER."""

    sip_headers: Optional[List[SipReferToolReferSipHeader]] = None
    """SIP headers to be added to the SIP REFER.

    Currently only User-to-User and Diversion headers are supported.
    """


class SipReferTool(BaseModel):
    refer: SipReferToolRefer

    type: Literal["refer"]


class DtmfTool(BaseModel):
    send_dtmf: Dict[str, object]

    type: Literal["send_dtmf"]


AssistantTool: TypeAlias = Union[
    WebhookTool, RetrievalTool, HandoffTool, HangupTool, TransferTool, SipReferTool, DtmfTool
]

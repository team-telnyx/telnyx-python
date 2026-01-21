# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .hangup_tool_param import HangupToolParam
from .retrieval_tool_param import RetrievalToolParam
from .inference_embedding_webhook_tool_params_param import InferenceEmbeddingWebhookToolParamsParam

__all__ = [
    "AssistantToolParam",
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
    InferenceEmbeddingWebhookToolParamsParam,
    RetrievalToolParam,
    Handoff,
    HangupToolParam,
    Transfer,
    Refer,
    SendDtmf,
    SendMessage,
]

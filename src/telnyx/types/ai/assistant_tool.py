# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .hangup_tool import HangupTool
from .retrieval_tool import RetrievalTool
from .inference_embedding_webhook_tool_params import InferenceEmbeddingWebhookToolParams

__all__ = [
    "AssistantTool",
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
    Union[
        InferenceEmbeddingWebhookToolParams, RetrievalTool, Handoff, HangupTool, Transfer, Refer, SendDtmf, SendMessage
    ],
    PropertyInfo(discriminator="type"),
]

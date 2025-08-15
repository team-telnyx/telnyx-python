# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .hangup_tool import HangupTool
from .webhook_tool import WebhookTool
from .transfer_tool import TransferTool
from .retrieval_tool import RetrievalTool

__all__ = [
    "AssistantTool",
    "HandoffTool",
    "HandoffToolHandoff",
    "HandoffToolHandoffAIAssistant",
    "SipReferTool",
    "SipReferToolRefer",
    "SipReferToolReferTarget",
    "SipReferToolReferCustomHeader",
    "SipReferToolReferSipHeader",
    "DtmfTool",
]


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

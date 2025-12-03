# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .hangup_tool_param import HangupToolParam
from .webhook_tool_param import WebhookToolParam
from .transfer_tool_param import TransferToolParam
from .retrieval_tool_param import RetrievalToolParam

__all__ = [
    "AssistantToolParam",
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
    WebhookToolParam, RetrievalToolParam, HandoffTool, HangupToolParam, TransferToolParam, SipReferTool, DtmfTool
]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .hangup_tool_param import HangupToolParam
from .webhook_tool_param import WebhookToolParam
from .transfer_tool_param import TransferToolParam
from ..shared_params.book_appointment_tool import BookAppointmentTool
from ..shared_params.check_availability_tool import CheckAvailabilityTool
from ..shared_params.call_control_retrieval_tool import CallControlRetrievalTool

__all__ = ["AssistantParam", "Tool"]

Tool: TypeAlias = Union[
    BookAppointmentTool,
    CheckAvailabilityTool,
    WebhookToolParam,
    HangupToolParam,
    TransferToolParam,
    CallControlRetrievalTool,
]


class AssistantParam(TypedDict, total=False):
    """
    Assistant configuration including choice of LLM, custom instructions, and tools.
    """

    instructions: str
    """The system instructions that the voice assistant uses during the gather command"""

    model: str
    """The model to be used by the voice assistant."""

    openai_api_key_ref: str
    """This is necessary only if the model selected is from OpenAI.

    You would pass the `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your OpenAI API Key. Warning: Free plans are unlikely to work
    with this integration.
    """

    tools: Iterable[Tool]
    """The tools that the voice assistant can use."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .hangup_tool_param import HangupToolParam
from .webhook_tool_param import WebhookToolParam
from .transfer_tool_param import TransferToolParam

__all__ = [
    "AssistantParam",
    "Tool",
    "ToolBookAppointmentTool",
    "ToolBookAppointmentToolBookAppointment",
    "ToolCheckAvailabilityTool",
    "ToolCheckAvailabilityToolCheckAvailability",
    "ToolCallControlRetrievalTool",
    "ToolCallControlRetrievalToolRetrieval",
]


class ToolBookAppointmentToolBookAppointment(TypedDict, total=False):
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


class ToolBookAppointmentTool(TypedDict, total=False):
    book_appointment: Required[ToolBookAppointmentToolBookAppointment]

    type: Required[Literal["book_appointment"]]


class ToolCheckAvailabilityToolCheckAvailability(TypedDict, total=False):
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


class ToolCheckAvailabilityTool(TypedDict, total=False):
    check_availability: Required[ToolCheckAvailabilityToolCheckAvailability]

    type: Required[Literal["check_availability"]]


class ToolCallControlRetrievalToolRetrieval(TypedDict, total=False):
    bucket_ids: Required[SequenceNotStr[str]]

    max_num_results: int
    """The maximum number of results to retrieve as context for the language model."""


class ToolCallControlRetrievalTool(TypedDict, total=False):
    retrieval: Required[ToolCallControlRetrievalToolRetrieval]

    type: Required[Literal["retrieval"]]


Tool: TypeAlias = Union[
    ToolBookAppointmentTool,
    ToolCheckAvailabilityTool,
    WebhookToolParam,
    HangupToolParam,
    TransferToolParam,
    ToolCallControlRetrievalTool,
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

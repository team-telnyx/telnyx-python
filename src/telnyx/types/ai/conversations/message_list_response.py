# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ..assistants.tests.test_suites.meta import Meta

__all__ = ["MessageListResponse", "Data", "DataToolCall", "DataToolCallFunction"]


class DataToolCallFunction(BaseModel):
    arguments: str
    """JSON-formatted arguments to pass to the function."""

    name: str
    """Name of the function to call."""


class DataToolCall(BaseModel):
    id: str
    """Unique identifier for the tool call."""

    function: DataToolCallFunction

    type: Literal["function"]
    """Type of the tool call."""


class Data(BaseModel):
    role: Literal["user", "assistant", "tool"]
    """The role of the message sender."""

    text: str
    """The message content. Can be null for tool calls."""

    created_at: Optional[datetime] = None
    """The datetime the message was created on the conversation.

    This does not necesarily correspond to the time the message was sent. The best
    field to use to determine the time the end user experienced the message is
    `sent_at`.
    """

    sent_at: Optional[datetime] = None
    """The datetime the message was sent to the end user."""

    tool_calls: Optional[List[DataToolCall]] = None
    """Optional tool calls made by the assistant."""


class MessageListResponse(BaseModel):
    data: List[Data]

    meta: Meta

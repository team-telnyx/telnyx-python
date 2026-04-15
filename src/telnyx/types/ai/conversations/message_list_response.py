# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["MessageListResponse", "ToolCall", "ToolCallFunction"]


class ToolCallFunction(BaseModel):
    arguments: str
    """JSON-formatted arguments to pass to the function."""

    name: str
    """Name of the function to call."""


class ToolCall(BaseModel):
    id: str
    """Unique identifier for the tool call."""

    function: ToolCallFunction

    type: Literal["function"]
    """Type of the tool call."""


class MessageListResponse(BaseModel):
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

    tool_calls: Optional[List[ToolCall]] = None
    """Optional tool calls made by the assistant."""

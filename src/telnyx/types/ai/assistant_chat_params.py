# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AssistantChatParams"]


class AssistantChatParams(TypedDict, total=False):
    content: Required[str]
    """The message content sent by the client to the assistant"""

    conversation_id: Required[str]
    """A unique identifier for the conversation thread, used to maintain context"""

    name: str
    """The optional display name of the user sending the message"""

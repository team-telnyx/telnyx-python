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

    stream: bool
    """
    When true, the response is streamed as Server-Sent Events (`text/event-stream`):
    `delta` events carry content fragments as they are generated, a final `done`
    event carries the full content plus `whatsapp_template`, and a terminal `error`
    event reports failures that happen after streaming started. When false
    (default), the response is a single JSON object.
    """

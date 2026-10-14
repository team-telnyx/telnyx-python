# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CallConversationEnded",
    "Payload",
    "PayloadMessage",
    "PayloadMessageToolCall",
    "PayloadMessageToolCallFunction",
]


class PayloadMessageToolCallFunction(BaseModel):
    arguments: Optional[str] = None
    """The arguments passed to the tool, as a JSON-encoded string."""

    name: Optional[str] = None
    """The name of the tool that was called."""


class PayloadMessageToolCall(BaseModel):
    id: Optional[str] = None
    """
    Identifier of the tool call, referenced by the matching tool result's
    `tool_call_id`.
    """

    function: Optional[PayloadMessageToolCallFunction] = None

    type: Optional[Literal["function"]] = None
    """The type of tool call."""


class PayloadMessage(BaseModel):
    content: Optional[str] = None
    """The text of the message.

    For a tool result, the tool output. May be absent on an assistant message that
    only contains `tool_calls`.
    """

    role: Optional[Literal["user", "assistant", "tool", "system", "developer"]] = None
    """The author of the message.

    `tool`, `system`, and `developer` only appear when
    `conversation_ended_full_history` is enabled. `system` and `developer` entries
    are informational (for example idle check-ins, voicemail prompts,
    participant-left notices, or messages added through the API); their wording is
    not a stable contract.
    """

    timestamp: Optional[datetime] = None
    """ISO 8601 datetime of when the message was added to the conversation."""

    tool_call_id: Optional[str] = None
    """The `id` of the tool call this message answers.

    Only present on `tool` messages when `conversation_ended_full_history` is
    enabled.
    """

    tool_calls: Optional[List[PayloadMessageToolCall]] = None
    """Tools the assistant called in this turn.

    Only present on `assistant` messages when `conversation_ended_full_history` is
    enabled.
    """


class Payload(BaseModel):
    assistant_id: Optional[str] = None
    """Unique identifier of the assistant involved in the call."""

    call_control_id: Optional[str] = None
    """Call ID used to issue commands via Call Control API."""

    call_leg_id: Optional[str] = None
    """ID that is unique to the call leg."""

    call_session_id: Optional[str] = None
    """ID that is unique to the call session (group of related call legs)."""

    calling_party_type: Optional[Literal["pstn", "sip"]] = None
    """The type of calling party connection."""

    client_state: Optional[str] = None
    """Base64-encoded state received from a command."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    conversation_id: Optional[str] = None
    """ID unique to the conversation or insight group generated for the call."""

    duration_sec: Optional[int] = None
    """Duration of the conversation in seconds."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The caller's number or identifier."""

    llm_model: Optional[str] = None
    """The large language model used during the conversation."""

    messages: Optional[List[PayloadMessage]] = None
    """The conversation transcript, in order.

    By default it contains only `user` and `assistant` text turns. When the
    assistant's `telephony_settings.conversation_ended_full_history` is `true`, it
    contains the full conversation history, including assistant tool calls, tool
    results, and `system` and `developer` entries. Redacted when data retention is
    disabled for the account.
    """

    reason: Optional[str] = None
    """Reason the conversation ended.

    For Conversation Relay, `customer_disconnect` indicates that the customer
    WebSocket disconnected.
    """

    stt_model: Optional[str] = None
    """The speech-to-text model used in the conversation."""

    to: Optional[str] = None
    """The callee's number or SIP address."""

    tts_model_id: Optional[str] = None
    """The model ID used for text-to-speech synthesis."""

    tts_provider: Optional[str] = None
    """The text-to-speech provider used in the call."""

    tts_voice_id: Optional[str] = None
    """Voice ID used for TTS."""


class CallConversationEnded(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the event."""

    created_at: Optional[datetime] = None
    """Timestamp when the event was created in the system."""

    event_type: Optional[Literal["call.conversation.ended"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[Payload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallConversationEndedWebhookEvent", "Data", "DataPayload"]


class DataPayload(BaseModel):
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


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the event."""

    created_at: Optional[datetime] = None
    """Timestamp when the event was created in the system."""

    event_type: Optional[Literal["call.conversation.ended"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallConversationEndedWebhookEvent(BaseModel):
    data: Optional[Data] = None

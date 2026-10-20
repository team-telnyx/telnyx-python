# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CallAnalyzedWebhookEvent",
    "Data",
    "DataPayload",
    "DataPayloadConversationInsight",
    "DataPayloadConversationInsightConversationInsight",
    "DataPayloadCost",
    "DataPayloadCostUnionMember0",
    "DataPayloadCostUnionMember0Breakdown",
    "DataPayloadRecording",
    "DataPayloadRecordingDownloadURLs",
]


class DataPayloadConversationInsightConversationInsight(BaseModel):
    insight_id: Optional[str] = None
    """Identifier of the insight template the result was generated from."""

    result: Optional[str] = None
    """The generated insight result."""


class DataPayloadConversationInsight(BaseModel):
    conversation_insights: Optional[List[DataPayloadConversationInsightConversationInsight]] = None
    """Generated insight results."""

    status: Optional[str] = None
    """Status of insight generation for this entry."""


class DataPayloadCostUnionMember0Breakdown(BaseModel):
    cost: Optional[str] = None
    """
    Total cost for this product across the call, in the currency given by
    `cost.currency`.
    """

    product: Optional[str] = None
    """
    The Telnyx product the cost line belongs to (for example `ai-voice-assistant`,
    `inference`, `callcontrol-cdrs`, `siptrunking-cdrs`, `recording-cdrs`).
    """


class DataPayloadCostUnionMember0(BaseModel):
    """
    The session's cost breakdown from Session Analysis, covering every product billed on the call: the AI Voice Assistant engine minutes (`ai-voice-assistant`), LLM inference tokens (`inference`), and call-control, SIP trunking, and recording lines. If cost data could not be retrieved after retries, this field carries the placeholder string `No cost data available.` instead of an object.
    """

    breakdown: Optional[List[DataPayloadCostUnionMember0Breakdown]] = None
    """Cost lines grouped by product."""

    currency: Optional[str] = None
    """The currency of the cost amounts."""

    total: Optional[str] = None
    """The total cost of the call, summed across every product in the breakdown."""


DataPayloadCost: TypeAlias = Union[DataPayloadCostUnionMember0, str]


class DataPayloadRecordingDownloadURLs(BaseModel):
    """Download URL per format. URLs are pre-signed and expire."""

    mp3: Optional[str] = None
    """Pre-signed URL for the mp3 recording file."""

    wav: Optional[str] = None
    """Pre-signed URL for the wav recording file."""


class DataPayloadRecording(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the recording."""

    channels: Optional[str] = None
    """The recording channel configuration."""

    download_urls: Optional[DataPayloadRecordingDownloadURLs] = None
    """Download URL per format. URLs are pre-signed and expire."""

    end_time: Optional[datetime] = None
    """ISO 8601 datetime of when the recording ended."""

    format: Optional[str] = None
    """The recording file format."""

    start_time: Optional[datetime] = None
    """ISO 8601 datetime of when the recording started."""


class DataPayload(BaseModel):
    assistant_id: Optional[str] = None
    """Unique identifier of the assistant involved in the call."""

    call_control_id: Optional[str] = None
    """Call ID used to issue commands via Call Control API."""

    call_leg_id: Optional[str] = None
    """ID that is unique to the call leg."""

    call_session_id: Optional[str] = None
    """ID that is unique to the call session (group of related call legs)."""

    client_state: Optional[str] = None
    """Base64-encoded state received from a command."""

    connection_id: Optional[str] = None
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    conversation_id: Optional[str] = None
    """ID unique to the conversation generated for the call."""

    conversation_insights: Optional[List[DataPayloadConversationInsight]] = None
    """
    The conversation's generated insights, when insight generation was enabled for
    the assistant and has completed. Each entry carries a `status` and the generated
    `conversation_insights` results. An empty array when the conversation has no
    generated insights; null when insight data could not be retrieved.
    """

    cost: Optional[DataPayloadCost] = None
    """
    The session's cost breakdown from Session Analysis, covering every product
    billed on the call: the AI Voice Assistant engine minutes
    (`ai-voice-assistant`), LLM inference tokens (`inference`), and call-control,
    SIP trunking, and recording lines. If cost data could not be retrieved after
    retries, this field carries the placeholder string `No cost data available.`
    instead of an object.
    """

    duration_sec: Optional[int] = None
    """Duration of the conversation in seconds."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The caller's number or identifier."""

    llm_model: Optional[str] = None
    """The large language model used during the conversation."""

    reason: Optional[str] = None
    """Reason the conversation ended."""

    recordings: Optional[List[DataPayloadRecording]] = None
    """Recordings created for the call.

    An empty array when the call had no recordings; null when recording data could
    not be retrieved.
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


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the event."""

    event_type: Optional[Literal["call.analyzed"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime of when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallAnalyzedWebhookEvent(BaseModel):
    data: Optional[Data] = None

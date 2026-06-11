# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .event_status import EventStatus
from .conversation_channel_type import ConversationChannelType

__all__ = ["ScheduledPhoneCallEventResponse", "CallAttempt", "CallSettings"]


class CallAttempt(BaseModel):
    """
    One row in `call_attempts` — captures the terminal outcome of a single dispatch.
    """

    attempt_number: int

    attempted_at: datetime

    call_status: str
    """Values: busy, canceled, no-answer, ringing, completed, failed, in-progress"""

    call_duration: Optional[int] = None
    """Duration of the call in seconds"""

    telnyx_call_control_id: Optional[str] = None


class CallSettings(BaseModel):
    """
    Per-call telephony overrides applied when a scheduled phone-call event
    dispatches. Phone-call events only. New per-call dispatch options should be
    added here rather than as top-level event fields.
    """

    sip_region: Optional[Literal["US", "Europe", "Canada", "Australia", "Middle East"]] = None
    """SIP region passed to Telnyx when initiating an outbound call.

    Values match the Telnyx TeXML `SipRegion` parameter exactly. Telnyx defaults to
    `US` when omitted.
    """


class ScheduledPhoneCallEventResponse(BaseModel):
    assistant_id: str

    scheduled_at_fixed_datetime: datetime

    telnyx_agent_target: str

    telnyx_conversation_channel: ConversationChannelType

    telnyx_end_user_target: str

    call_attempts: Optional[List[CallAttempt]] = None

    call_duration: Optional[int] = None
    """Duration of the call in seconds"""

    call_settings: Optional[CallSettings] = None
    """
    Per-call telephony overrides applied when a scheduled phone-call event
    dispatches. Phone-call events only. New per-call dispatch options should be
    added here rather than as top-level event fields.
    """

    call_status: Optional[str] = None
    """Values: busy, canceled, no-answer, ringing, completed, failed, in-progress"""

    conversation_id: Optional[str] = None

    conversation_metadata: Optional[Dict[str, Union[str, int, bool]]] = None

    created_at: Optional[datetime] = None

    dispatched_at: Optional[datetime] = None
    """Date time at which call was sent"""

    dynamic_variables: Optional[Dict[str, str]] = None
    """A map of dynamic variable names to values.

    These variables can be referenced in the assistant's instructions and messages
    using {{variable_name}} syntax.
    """

    errors: Optional[List[str]] = None

    max_retries_client_errors: Optional[int] = None
    """
    Configure number of retries on client errors: busy, no-answer, failed, canceled
    (caller hung up before the callee answered)
    """

    retry_attempts: Optional[int] = None

    retry_count: Optional[int] = None

    retry_interval_secs: Optional[int] = None

    scheduled_event_id: Optional[str] = None

    status: Optional[EventStatus] = None

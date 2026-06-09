# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .conversation_channel_type import ConversationChannelType

__all__ = ["ScheduledEventCreateParams", "CallSettings"]


class ScheduledEventCreateParams(TypedDict, total=False):
    scheduled_at_fixed_datetime: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The datetime at which the event should be scheduled. Formatted as ISO 8601."""

    telnyx_agent_target: Required[str]
    """The phone number, SIP URI, to schedule the call or text from."""

    telnyx_conversation_channel: Required[ConversationChannelType]

    telnyx_end_user_target: Required[str]
    """The phone number, SIP URI, to schedule the call or text to."""

    call_settings: CallSettings
    """
    Per-call telephony overrides applied when a scheduled phone-call event
    dispatches. Phone-call events only. New per-call dispatch options should be
    added here rather than as top-level event fields.
    """

    conversation_metadata: Dict[str, Union[str, int, bool]]
    """Metadata associated with the conversation.

    Telnyx provides several pieces of metadata, but customers can also add their
    own.
    """

    dynamic_variables: Dict[str, str]
    """A map of dynamic variable names to values.

    These variables can be referenced in the assistant's instructions and messages
    using {{variable_name}} syntax.
    """

    max_retries_client_errors: int
    """
    Configure number of retries on client errors: busy, no-answer, failed, canceled
    (caller hung up before the callee answered)
    """

    retry_interval_secs: int

    text: str
    """Required for sms scheduled events. The text to be sent to the end user."""


class CallSettings(TypedDict, total=False):
    """
    Per-call telephony overrides applied when a scheduled phone-call event
    dispatches. Phone-call events only. New per-call dispatch options should be
    added here rather than as top-level event fields.
    """

    sip_region: Literal["US", "Europe", "Canada", "Australia", "Middle East"]
    """SIP region passed to Telnyx when initiating an outbound call.

    Values match the Telnyx TeXML `SipRegion` parameter exactly. Telnyx defaults to
    `US` when omitted.
    """

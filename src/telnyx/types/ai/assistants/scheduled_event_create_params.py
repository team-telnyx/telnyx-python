# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .conversation_channel_type import ConversationChannelType

__all__ = ["ScheduledEventCreateParams"]


class ScheduledEventCreateParams(TypedDict, total=False):
    scheduled_at_fixed_datetime: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The datetime at which the event should be scheduled. Formatted as ISO 8601."""

    telnyx_agent_target: Required[str]
    """The phone number, SIP URI, to schedule the call or text from."""

    telnyx_conversation_channel: Required[ConversationChannelType]

    telnyx_end_user_target: Required[str]
    """The phone number, SIP URI, to schedule the call or text to."""

    conversation_metadata: Dict[str, Union[str, int, bool]]
    """Metadata associated with the conversation.

    Telnyx provides several pieces of metadata, but customers can also add their
    own.
    """

    text: str
    """Required for sms scheduled events. The text to be sent to the end user."""

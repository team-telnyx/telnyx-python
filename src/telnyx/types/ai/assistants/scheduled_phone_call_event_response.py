# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from ...._models import BaseModel
from .event_status import EventStatus
from .conversation_channel_type import ConversationChannelType

__all__ = ["ScheduledPhoneCallEventResponse"]


class ScheduledPhoneCallEventResponse(BaseModel):
    assistant_id: str

    scheduled_at_fixed_datetime: datetime

    telnyx_agent_target: str

    telnyx_conversation_channel: ConversationChannelType

    telnyx_end_user_target: str

    conversation_id: Optional[str] = None

    conversation_metadata: Optional[Dict[str, Union[str, int, bool]]] = None

    created_at: Optional[datetime] = None

    dynamic_variables: Optional[Dict[str, str]] = None
    """A map of dynamic variable names to values.

    These variables can be referenced in the assistant's instructions and messages
    using {{variable_name}} syntax.
    """

    errors: Optional[List[str]] = None

    retry_attempts: Optional[int] = None

    retry_count: Optional[int] = None

    scheduled_event_id: Optional[str] = None

    status: Optional[EventStatus] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ...._utils import PropertyInfo
from .scheduled_sms_event_response import ScheduledSMSEventResponse
from .scheduled_phone_call_event_response import ScheduledPhoneCallEventResponse

__all__ = ["ScheduledEventListResponse"]

ScheduledEventListResponse: TypeAlias = Annotated[
    Union[ScheduledPhoneCallEventResponse, ScheduledSMSEventResponse],
    PropertyInfo(discriminator="telnyx_conversation_channel"),
]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .scheduled_sms_event_response import ScheduledSMSEventResponse
from .scheduled_phone_call_event_response import ScheduledPhoneCallEventResponse

__all__ = ["ScheduledEventResponse"]

ScheduledEventResponse: TypeAlias = Union[ScheduledPhoneCallEventResponse, ScheduledSMSEventResponse]

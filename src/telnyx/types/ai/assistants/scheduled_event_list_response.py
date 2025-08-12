# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from ...._models import BaseModel
from .tests.test_suites.meta import Meta
from .scheduled_sms_event_response import ScheduledSMSEventResponse
from .scheduled_phone_call_event_response import ScheduledPhoneCallEventResponse

__all__ = ["ScheduledEventListResponse", "Data"]

Data: TypeAlias = Union[ScheduledPhoneCallEventResponse, ScheduledSMSEventResponse]


class ScheduledEventListResponse(BaseModel):
    data: List[Data]

    meta: Meta

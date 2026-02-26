# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .event_data import EventData
from ....._models import BaseModel

__all__ = ["EventLogResponse"]


class EventLogResponse(BaseModel):
    data: EventData

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .event_data import EventData
from ....._models import BaseModel

__all__ = ["EventResponse"]


class EventResponse(BaseModel):
    data: EventData

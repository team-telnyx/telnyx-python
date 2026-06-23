# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .portout_event import PortoutEvent

__all__ = ["EventRetrieveResponse"]


class EventRetrieveResponse(BaseModel):
    data: Optional[PortoutEvent] = None

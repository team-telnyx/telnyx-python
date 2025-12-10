# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["CallEventListResponse", "Data"]


class Data(BaseModel):
    call_leg_id: str
    """Uniquely identifies an individual call leg."""

    call_session_id: str
    """Uniquely identifies the call control session.

    A session may include multiple call leg events.
    """

    event_timestamp: str
    """Event timestamp"""

    metadata: object
    """
    Event metadata, which includes raw event, and extra information based on event
    type
    """

    name: str
    """Event name"""

    record_type: Literal["call_event"]

    type: Literal["command", "webhook"]
    """Event type"""


class CallEventListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

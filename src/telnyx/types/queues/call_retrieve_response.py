# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CallRetrieveResponse", "Data"]


class Data(BaseModel):
    call_control_id: str
    """Unique identifier and token for controlling the call."""

    call_leg_id: str
    """ID that is unique to the call and can be used to correlate webhook events"""

    call_session_id: str
    """
    ID that is unique to the call session and can be used to correlate webhook
    events. Call session is a group of related call legs that logically belong to
    the same phone call, e.g. an inbound and outbound leg of a transferred call
    """

    connection_id: str
    """Call Control App ID (formerly Telnyx connection ID) used in the call."""

    enqueued_at: str
    """ISO 8601 formatted date of when the call was put in the queue"""

    from_: str = FieldInfo(alias="from")
    """Number or SIP URI placing the call."""

    queue_id: str
    """Unique identifier of the queue the call is in."""

    queue_position: int
    """Current position of the call in the queue"""

    record_type: Literal["queue_call"]

    to: str
    """Destination number or SIP URI of the call."""

    wait_time_secs: int
    """The time the call has been waiting in the queue, given in seconds"""


class CallRetrieveResponse(BaseModel):
    data: Optional[Data] = None

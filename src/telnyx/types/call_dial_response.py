# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CallDialResponse", "Data"]


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

    is_alive: bool
    """Indicates whether the call is alive or not.

    For Dial command it will always be `false` (dialing is asynchronous).
    """

    record_type: Literal["call"]

    call_duration: Optional[int] = None
    """Indicates the duration of the call in seconds"""

    client_state: Optional[str] = None
    """State received from a command."""

    end_time: Optional[str] = None
    """ISO 8601 formatted date indicating when the call ended.

    Only present when the call is not alive
    """

    recording_id: Optional[str] = None
    """The ID of the recording.

    Only present when the record parameter is set to record-from-answer.
    """

    start_time: Optional[str] = None
    """ISO 8601 formatted date indicating when the call started"""


class CallDialResponse(BaseModel):
    data: Optional[Data] = None

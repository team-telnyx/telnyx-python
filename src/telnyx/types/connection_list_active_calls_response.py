# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectionListActiveCallsResponse"]


class ConnectionListActiveCallsResponse(BaseModel):
    call_control_id: str
    """Unique identifier and token for controlling the call."""

    call_duration: int
    """Indicates the duration of the call in seconds"""

    call_leg_id: str
    """ID that is unique to the call and can be used to correlate webhook events"""

    call_session_id: str
    """
    ID that is unique to the call session and can be used to correlate webhook
    events. Call session is a group of related call legs that logically belong to
    the same phone call, e.g. an inbound and outbound leg of a transferred call
    """

    client_state: str
    """State received from a command."""

    record_type: Literal["call"]

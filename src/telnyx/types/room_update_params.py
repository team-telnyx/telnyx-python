# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["RoomUpdateParams"]


class RoomUpdateParams(TypedDict, total=False):
    enable_recording: bool
    """Enable or disable recording for that room."""

    max_participants: int
    """The maximum amount of participants allowed in a room.

    If new participants try to join after that limit is reached, their request will
    be rejected.
    """

    unique_name: str
    """The unique (within the Telnyx account scope) name of the room."""

    webhook_event_failover_url: Optional[str]
    """
    The failover URL where webhooks related to this room will be sent if sending to
    the primary URL fails. Must include a scheme, such as 'https'.
    """

    webhook_event_url: str
    """The URL where webhooks related to this room will be sent.

    Must include a scheme, such as 'https'.
    """

    webhook_timeout_secs: Optional[int]
    """Specifies how many seconds to wait before timing out a webhook."""

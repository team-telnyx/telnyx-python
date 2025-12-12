# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConferenceListParticipantsResponse", "Conference"]


class Conference(BaseModel):
    """Info about the conference that the participant is in"""

    id: Optional[str] = None
    """Uniquely identifies the conference"""

    name: Optional[str] = None
    """Name of the conference"""


class ConferenceListParticipantsResponse(BaseModel):
    id: str
    """Uniquely identifies the participant"""

    call_control_id: str
    """Call Control ID associated with the partiipant of the conference"""

    call_leg_id: str
    """Uniquely identifies the call leg associated with the participant"""

    conference: Conference
    """Info about the conference that the participant is in"""

    created_at: str
    """ISO 8601 formatted date of when the participant was created"""

    end_conference_on_exit: bool
    """
    Whether the conference will end and all remaining participants be hung up after
    the participant leaves the conference.
    """

    muted: bool
    """Whether the participant is muted."""

    on_hold: bool
    """Whether the participant is put on_hold."""

    record_type: Literal["participant"]

    soft_end_conference_on_exit: bool
    """Whether the conference will end after the participant leaves the conference."""

    status: Literal["joining", "joined", "left"]
    """
    The status of the participant with respect to the lifecycle within the
    conference
    """

    updated_at: str
    """ISO 8601 formatted date of when the participant was last updated"""

    whisper_call_control_ids: List[str]
    """Array of unique call_control_ids the participant can whisper to.."""

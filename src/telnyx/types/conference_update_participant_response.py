# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConferenceUpdateParticipantResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the participant."""

    call_control_id: Optional[str] = None
    """Unique identifier and token for controlling the participant's call leg."""

    call_leg_id: Optional[str] = None
    """Unique identifier for the call leg."""

    conference_id: Optional[str] = None
    """Unique identifier for the conference."""

    created_at: Optional[datetime] = None
    """Timestamp when the participant joined."""

    end_conference_on_exit: Optional[bool] = None
    """Whether the conference ends when this participant exits."""

    label: Optional[str] = None
    """Label assigned to the participant when joining."""

    muted: Optional[bool] = None
    """Whether the participant is muted."""

    on_hold: Optional[bool] = None
    """Whether the participant is on hold."""

    soft_end_conference_on_exit: Optional[bool] = None
    """Whether the conference soft-ends when this participant exits."""

    status: Optional[Literal["joining", "joined", "left"]] = None
    """Status of the participant."""

    updated_at: Optional[datetime] = None
    """Timestamp when the participant was last updated."""

    whisper_call_control_ids: Optional[List[str]] = None
    """List of call control IDs this participant is whispering to."""


class ConferenceUpdateParticipantResponse(BaseModel):
    data: Optional[Data] = None

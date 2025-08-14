# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["ParticipantParticipantsResponse"]


class ParticipantParticipantsResponse(BaseModel):
    account_sid: Optional[str] = None
    """The id of the account the resource belongs to."""

    call_sid: Optional[str] = None
    """The identifier of this participant's call."""

    coaching: Optional[bool] = None
    """Whether the participant is coaching another call."""

    coaching_call_sid: Optional[str] = None
    """The identifier of the coached participant's call."""

    end_conference_on_exit: Optional[bool] = None
    """Whether the conference ends when the participant leaves."""

    hold: Optional[bool] = None
    """Whether the participant is on hold."""

    muted: Optional[bool] = None
    """Whether the participant is muted."""

    status: Optional[Literal["connecting", "connected", "completed"]] = None
    """The status of the participant's call in the conference."""

    uri: Optional[str] = None
    """The relative URI for this participant."""

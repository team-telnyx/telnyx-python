# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["ParticipantRetrieveParticipantsResponse", "Participant"]


class Participant(BaseModel):
    account_sid: Optional[str] = None
    """The id of the account the resource belongs to."""

    api_version: Optional[str] = None
    """The version of the API that was used to make the request."""

    call_sid: Optional[str] = None
    """The identifier of this participant's call."""

    call_sid_legacy: Optional[str] = None
    """The identifier of this participant's call."""

    coaching: Optional[bool] = None
    """Whether the participant is coaching another call."""

    coaching_call_sid: Optional[str] = None
    """The identifier of the coached participant's call."""

    coaching_call_sid_legacy: Optional[str] = None
    """The identifier of the coached participant's call."""

    date_created: Optional[str] = None
    """The timestamp of when the resource was created."""

    date_updated: Optional[str] = None
    """The timestamp of when the resource was last updated."""

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


class ParticipantRetrieveParticipantsResponse(BaseModel):
    end: Optional[int] = None
    """The number of the last element on the page, zero-indexed."""

    first_page_uri: Optional[str] = None
    """
    /v2/texml/Accounts/61bf923e-5e4d-4595-a110-56190ea18a1b/Conferences/6dc6cc1a-1ba1-4351-86b8-4c22c95cd98f/Participants.json?page=0&pagesize=20
    """

    next_page_uri: Optional[str] = None
    """
    /v2/texml/Accounts/61bf923e-5e4d-4595-a110-56190ea18a1b/Conferences/6dc6cc1a-1ba1-4351-86b8-4c22c95cd98f/Participants.json?Page=1&PageSize=1&PageToken=MTY4AjgyNDkwNzIxMQ
    """

    page: Optional[int] = None
    """Current page number, zero-indexed."""

    page_size: Optional[int] = None
    """The number of items on the page"""

    participants: Optional[List[Participant]] = None

    start: Optional[int] = None
    """The number of the first element on the page, zero-indexed."""

    uri: Optional[str] = None
    """The URI of the current page."""

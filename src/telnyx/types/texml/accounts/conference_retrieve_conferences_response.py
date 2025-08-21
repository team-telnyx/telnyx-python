# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ConferenceRetrieveConferencesResponse", "Conference"]


class Conference(BaseModel):
    account_sid: Optional[str] = None
    """The id of the account the resource belongs to."""

    api_version: Optional[str] = None
    """The version of the API that was used to make the request."""

    call_sid_ending_conference: Optional[str] = None
    """Caller ID, if present."""

    date_created: Optional[str] = None
    """The timestamp of when the resource was created."""

    date_updated: Optional[str] = None
    """The timestamp of when the resource was last updated."""

    friendly_name: Optional[str] = None
    """A string that you assigned to describe this conference room."""

    reason_conference_ended: Optional[
        Literal[
            "participant-with-end-conference-on-exit-left",
            "last-participant-left",
            "conference-ended-via-api",
            "time-exceeded",
        ]
    ] = None
    """The reason why a conference ended.

    When a conference is in progress, will be null.
    """

    region: Optional[str] = None
    """A string representing the region where the conference is hosted."""

    sid: Optional[str] = None
    """The unique identifier of the conference."""

    status: Optional[Literal["init", "in-progress", "completed"]] = None
    """The status of this conference."""

    subresource_uris: Optional[Dict[str, object]] = None
    """A list of related resources identified by their relative URIs."""

    uri: Optional[str] = None
    """The relative URI for this conference."""


class ConferenceRetrieveConferencesResponse(BaseModel):
    conferences: Optional[List[Conference]] = None

    end: Optional[int] = None
    """The number of the last element on the page, zero-indexed."""

    first_page_uri: Optional[str] = None
    """
    /v2/texml/Accounts/61bf923e-5e4d-4595-a110-56190ea18a1b/Conferences.json?Page=0&PageSize=1
    """

    next_page_uri: Optional[str] = None
    """
    /v2/texml/Accounts/61bf923e-5e4d-4595-a110-56190ea18a1b/Conferences.json?Page=1&PageSize=1&PageToken=MTY4AjgyNDkwNzIxMQ
    """

    page: Optional[int] = None
    """Current page number, zero-indexed."""

    page_size: Optional[int] = None
    """The number of items on the page"""

    start: Optional[int] = None
    """The number of the first element on the page, zero-indexed."""

    uri: Optional[str] = None
    """The URI of the current page."""

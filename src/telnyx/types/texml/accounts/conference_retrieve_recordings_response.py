# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ConferenceRetrieveRecordingsResponse", "Recording"]


class Recording(BaseModel):
    account_sid: Optional[str] = None
    """The id of the account the resource belongs to."""

    call_sid: Optional[str] = None
    """The identifier of the related participant's call."""

    channels: Optional[int] = None
    """The number of channels in the recording."""

    conference_sid: Optional[str] = None
    """The identifier of the related conference."""

    date_created: Optional[str] = None
    """The timestamp of when the resource was created."""

    date_updated: Optional[str] = None
    """The timestamp of when the resource was last updated."""

    duration: Optional[int] = None
    """Duratin of the recording in seconds."""

    error_code: Optional[str] = None
    """The recording error, if any."""

    media_url: Optional[str] = None
    """The URL to use to download the recording."""

    sid: Optional[str] = None
    """The unique identifier of the recording."""

    source: Optional[
        Literal[
            "DialVerb",
            "Conference",
            "OutboundAPI",
            "Trunking",
            "RecordVerb",
            "StartCallRecordingAPI",
            "StartConferenceRecordingAPI",
        ]
    ] = None
    """How the recording was started."""

    start_time: Optional[str] = None
    """The timestamp of when the recording was started."""

    status: Optional[Literal["processing", "absent", "completed", "deleted"]] = None
    """The status of the recording."""

    subresource_uris: Optional[Dict[str, object]] = None
    """A list of related resources identified by their relative URIs."""

    uri: Optional[str] = None
    """The relative URI for this recording."""


class ConferenceRetrieveRecordingsResponse(BaseModel):
    end: Optional[int] = None
    """The number of the last element on the page, zero-indexed."""

    first_page_uri: Optional[str] = None
    """
    /v2/texml/Accounts/61bf923e-5e4d-4595-a110-56190ea18a1b/Conferences/6dc6cc1a-1ba1-4351-86b8-4c22c95cd98f/Recordings.json?page=0&pagesize=20
    """

    next_page_uri: Optional[str] = None
    """
    /v2/texml/Accounts/61bf923e-5e4d-4595-a110-56190ea18a1b/Conferences/6dc6cc1a-1ba1-4351-86b8-4c22c95cd98f/Recordings.json?Page=1&PageSize=1&PageToken=MTY4AjgyNDkwNzIxMQ
    """

    page: Optional[int] = None
    """Current page number, zero-indexed."""

    page_size: Optional[int] = None
    """The number of items on the page"""

    recordings: Optional[List[Recording]] = None

    start: Optional[int] = None
    """The number of the first element on the page, zero-indexed."""

    uri: Optional[str] = None
    """The URI of the current page."""

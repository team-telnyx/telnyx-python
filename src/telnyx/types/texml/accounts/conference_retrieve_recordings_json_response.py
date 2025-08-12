# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ConferenceRetrieveRecordingsJsonResponse", "Recording", "RecordingSubresourcesUris"]


class RecordingSubresourcesUris(BaseModel):
    transcriptions: Optional[str] = None


class Recording(BaseModel):
    account_sid: Optional[str] = None

    call_sid: Optional[str] = None

    channels: Optional[Literal[1, 2]] = None

    conference_sid: Optional[str] = None

    date_created: Optional[datetime] = None

    date_updated: Optional[datetime] = None

    duration: Optional[str] = None
    """The duration of this recording, given in seconds."""

    error_code: Optional[str] = None

    media_url: Optional[str] = None

    sid: Optional[str] = None
    """Identifier of a resource."""

    source: Optional[
        Literal[
            "StartCallRecordingAPI",
            "StartConferenceRecordingAPI",
            "OutboundAPI",
            "DialVerb",
            "Conference",
            "RecordVerb",
            "Trunking",
        ]
    ] = None
    """Defines how the recording was created."""

    start_time: Optional[datetime] = None

    status: Optional[Literal["in-progress", "completed", "paused", "stopped"]] = None

    subresources_uris: Optional[RecordingSubresourcesUris] = None
    """Subresources details for a recording if available."""

    uri: Optional[str] = None
    """The relative URI for this recording resource."""


class ConferenceRetrieveRecordingsJsonResponse(BaseModel):
    end: Optional[int] = None
    """The number of the last element on the page, zero-indexed."""

    first_page_uri: Optional[str] = None
    """Relative uri to the first page of the query results"""

    next_page_uri: Optional[str] = None
    """Relative uri to the next page of the query results"""

    page: Optional[int] = None
    """Current page number, zero-indexed."""

    page_size: Optional[int] = None
    """The number of items on the page"""

    previous_page_uri: Optional[str] = None
    """Relative uri to the previous page of the query results"""

    recordings: Optional[List[Recording]] = None

    start: Optional[int] = None
    """The number of the first element on the page, zero-indexed."""

    uri: Optional[str] = None
    """The URI of the current page."""

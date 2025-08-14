# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountRetrieveTranscriptionsJsonResponse", "Transcription"]


class Transcription(BaseModel):
    account_sid: Optional[str] = None

    api_version: Optional[str] = None
    """The version of the API that was used to make the request."""

    call_sid: Optional[str] = None

    date_created: Optional[datetime] = None

    date_updated: Optional[datetime] = None

    duration: Optional[str] = None
    """The duration of this recording, given in seconds."""

    recording_sid: Optional[str] = None
    """Identifier of a resource."""

    sid: Optional[str] = None
    """Identifier of a resource."""

    status: Optional[Literal["in-progress", "completed"]] = None
    """The status of the recording transcriptions.

    The transcription text will be available only when the status is completed.
    """

    transcription_text: Optional[str] = None
    """The recording's transcribed text"""

    uri: Optional[str] = None
    """The relative URI for the recording transcription resource."""


class AccountRetrieveTranscriptionsJsonResponse(BaseModel):
    end: Optional[int] = None
    """The number of the last element on the page, zero-indexed"""

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

    start: Optional[int] = None
    """The number of the first element on the page, zero-indexed."""

    transcriptions: Optional[List[Transcription]] = None

    uri: Optional[str] = None
    """The URI of the current page."""

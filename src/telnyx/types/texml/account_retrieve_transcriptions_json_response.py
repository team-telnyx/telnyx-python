# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .accounts.transcriptions.texml_recording_transcription import TexmlRecordingTranscription

__all__ = ["AccountRetrieveTranscriptionsJsonResponse"]


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

    transcriptions: Optional[List[TexmlRecordingTranscription]] = None

    uri: Optional[str] = None
    """The URI of the current page."""

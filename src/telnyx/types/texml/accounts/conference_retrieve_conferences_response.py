# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel
from .conference_resource import ConferenceResource

__all__ = ["ConferenceRetrieveConferencesResponse"]


class ConferenceRetrieveConferencesResponse(BaseModel):
    conferences: Optional[List[ConferenceResource]] = None

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

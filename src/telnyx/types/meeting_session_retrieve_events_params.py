# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MeetingSessionRetrieveEventsParams"]


class MeetingSessionRetrieveEventsParams(TypedDict, total=False):
    after: int
    """Return results with a cursor position after this value."""

    limit: int
    """Maximum number of results to return per page."""

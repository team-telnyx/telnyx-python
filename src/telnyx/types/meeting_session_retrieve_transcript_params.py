# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MeetingSessionRetrieveTranscriptParams"]


class MeetingSessionRetrieveTranscriptParams(TypedDict, total=False):
    after: int
    """Return results with a cursor position after this value."""

    limit: int
    """Maximum number of results to return per page."""

    wait_seconds: int
    """Long-poll duration in seconds.

    The server holds the connection open for up to this many seconds, waiting for
    new or updated results before returning an empty response. Set to 0 for an
    immediate response.
    """

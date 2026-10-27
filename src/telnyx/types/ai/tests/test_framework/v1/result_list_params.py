# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ResultListParams"]


class ResultListParams(TypedDict, total=False):
    agent_id: int
    """Filter results belonging to the specified test agent."""

    page: int
    """Page number (1-based)."""

    page_size: int
    """Number of results per page."""

    scenarios: str
    """Filter results by a comma-separated list of scenario IDs."""

    search: str
    """Filter results by a search string."""

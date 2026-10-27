# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ScenarioListParams"]


class ScenarioListParams(TypedDict, total=False):
    agent_id: int
    """Filter scenarios belonging to the specified test agent."""

    assistant_id: str
    """Filter scenarios belonging to the specified Telnyx assistant."""

    page: int
    """Page number (1-based)."""

    page_size: int
    """Number of results per page."""

    tags: str
    """Filter scenarios by a comma-separated list of tags."""

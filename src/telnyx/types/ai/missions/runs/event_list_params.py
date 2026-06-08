# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    mission_id: Required[str]

    agent_id: str
    """Filter results by agent id."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number (1-based)"""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of items per page"""

    step_id: str
    """Filter results by step id."""

    type: str
    """Filter results by type."""

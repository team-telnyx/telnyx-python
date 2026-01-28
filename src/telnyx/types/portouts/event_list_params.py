# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EventListParams", "Filter", "FilterCreatedAt"]


class EventListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[event_type], filter[portout_id], filter[created_at]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class FilterCreatedAt(TypedDict, total=False):
    """Filter by created_at date range using nested operations"""

    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by created at greater than or equal to."""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by created at less than or equal to."""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[event_type], filter[portout_id], filter[created_at]
    """

    created_at: FilterCreatedAt
    """Filter by created_at date range using nested operations"""

    event_type: Literal["portout.status_changed", "portout.new_comment", "portout.foc_date_changed"]
    """Filter by event type."""

    portout_id: str
    """Filter by port-out order ID."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EventListParams", "Filter", "FilterCreatedAt", "Page"]


class EventListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[type], filter[porting_order_id], filter[created_at][gte],
    filter[created_at][lte]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterCreatedAt(TypedDict, total=False):
    gte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by created at greater than or equal to."""

    lte: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by created at less than or equal to."""


class Filter(TypedDict, total=False):
    created_at: FilterCreatedAt
    """Created at date range filtering operations"""

    porting_order_id: str
    """Filter by porting order ID."""

    type: Literal[
        "porting_order.deleted",
        "porting_order.loa_updated",
        "porting_order.messaging_changed",
        "porting_order.status_changed",
        "porting_order.sharing_token_expired",
        "porting_order.new_comment",
        "porting_order.split",
    ]
    """Filter by event type."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallRetrieveCallsParams"]


class CallRetrieveCallsParams(TypedDict, total=False):
    end_time: Annotated[str, PropertyInfo(alias="EndTime")]
    """Filters calls by their end date. Expected format is YYYY-MM-DD"""

    end_time_gt: Annotated[str, PropertyInfo(alias="EndTime_gt")]
    """Filters calls by their end date (after). Expected format is YYYY-MM-DD"""

    end_time_lt: Annotated[str, PropertyInfo(alias="EndTime_lt")]
    """Filters calls by their end date (before). Expected format is YYYY-MM-DD"""

    from_: Annotated[str, PropertyInfo(alias="From")]
    """Filters calls by the from number."""

    page: Annotated[int, PropertyInfo(alias="Page")]
    """
    The number of the page to be displayed, zero-indexed, should be used in
    conjuction with PageToken.
    """

    page_size: Annotated[int, PropertyInfo(alias="PageSize")]
    """The number of records to be displayed on a page"""

    page_token: Annotated[str, PropertyInfo(alias="PageToken")]
    """Used to request the next page of results."""

    start_time: Annotated[str, PropertyInfo(alias="StartTime")]
    """Filters calls by their start date. Expected format is YYYY-MM-DD."""

    start_time_gt: Annotated[str, PropertyInfo(alias="StartTime_gt")]
    """Filters calls by their start date (after). Expected format is YYYY-MM-DD"""

    start_time_lt: Annotated[str, PropertyInfo(alias="StartTime_lt")]
    """Filters calls by their start date (before). Expected format is YYYY-MM-DD"""

    status: Annotated[Literal["canceled", "completed", "failed", "busy", "no-answer"], PropertyInfo(alias="Status")]
    """Filters calls by status."""

    to: Annotated[str, PropertyInfo(alias="To")]
    """Filters calls by the to number."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UsageRetrieveSummaryParams"]


class UsageRetrieveSummaryParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Exclusive UTC date in YYYY-MM-DD format.

    Must follow start_date by 1 to 31 days.
    """

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Inclusive UTC date in YYYY-MM-DD format. Must precede end_date by 1 to 31 days."""

    token_group_id: Required[str]
    """ID of a token group owned by the authenticated account."""

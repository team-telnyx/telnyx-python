# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UsageGetAPIUsageParams", "Filter"]


class UsageGetAPIUsageParams(TypedDict, total=False):
    filter: Required[Filter]
    """Consolidated filter parameter (deepObject style).

    Originally: filter[start_time], filter[end_time]
    """


class Filter(TypedDict, total=False):
    end_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The end time of the period to filter the usage (ISO microsecond format)"""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The start time of the period to filter the usage (ISO microsecond format)"""

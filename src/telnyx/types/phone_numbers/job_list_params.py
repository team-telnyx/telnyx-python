# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JobListParams", "Filter"]


class JobListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style). Originally: filter[type]"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Literal["created_at"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style). Originally: filter[type]"""

    type: Literal["update_emergency_settings", "delete_phone_numbers", "update_phone_numbers"]
    """Identifies the type of the background job."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["JobListParams", "Filter", "Page"]


class JobListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style). Originally: filter[type]"""

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: Literal["created_at"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """


class Filter(TypedDict, total=False):
    type: Literal["update_emergency_settings", "delete_phone_numbers", "update_phone_numbers"]
    """Identifies the type of the background job."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

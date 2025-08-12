# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["VerificationCodeListParams", "Filter", "Page", "Sort"]


class VerificationCodeListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style). Originally: filter[verified]"""

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: Sort
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""


class Filter(TypedDict, total=False):
    verified: bool
    """Filter verification codes that have been verified or not"""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""


class Sort(TypedDict, total=False):
    value: Literal["created_at", "-created_at"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """

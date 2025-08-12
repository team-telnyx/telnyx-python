# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AssociatedPhoneNumberListParams", "Filter", "Page", "Sort"]


class AssociatedPhoneNumberListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[phone_number], filter[action]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: Sort
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""


class Filter(TypedDict, total=False):
    action: Literal["keep", "disconnect"]
    """Filter results by action type"""

    phone_number: str
    """Filter results by a phone number. It should be in E.164 format."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""


class Sort(TypedDict, total=False):
    value: Literal["-created_at", "created_at"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order
    """

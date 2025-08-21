# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VerifyProfileListParams", "Filter", "Page"]


class VerifyProfileListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style). Originally: filter[name]"""

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class Filter(TypedDict, total=False):
    name: str
    """Optional filter for profile names."""


class Page(TypedDict, total=False):
    number: int

    size: int

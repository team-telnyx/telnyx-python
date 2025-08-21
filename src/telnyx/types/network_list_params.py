# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NetworkListParams", "Filter", "Page"]


class NetworkListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style). Originally: filter[name]"""

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """


class Filter(TypedDict, total=False):
    name: str
    """The network name to filter on."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CallListParams", "Page"]


class CallListParams(TypedDict, total=False):
    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[after], page[before], page[limit], page[size], page[number]
    """


class Page(TypedDict, total=False):
    after: str
    """Opaque identifier of next page"""

    before: str
    """Opaque identifier of previous page"""

    limit: int
    """Limit of records per single page"""

    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

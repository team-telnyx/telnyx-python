# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PortingOrderRetrieveRequirementsParams", "Page"]


class PortingOrderRetrieveRequirementsParams(TypedDict, total=False):
    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

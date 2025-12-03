# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InsightGroupRetrieveInsightGroupsParams", "Page"]


class InsightGroupRetrieveInsightGroupsParams(TypedDict, total=False):
    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """


class Page(TypedDict, total=False):
    number: int
    """Page number (0-based)"""

    size: int
    """Number of items per page"""

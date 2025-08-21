# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VerifiedNumberListParams", "Page"]


class VerifiedNumberListParams(TypedDict, total=False):
    page: Page
    """Consolidated page parameter (deepObject style).

    Use page[size] and page[number] in the query string. Originally: page[size],
    page[number]
    """


class Page(TypedDict, total=False):
    number: int

    size: int

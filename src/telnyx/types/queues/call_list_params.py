# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CallListParams", "Page"]


class CallListParams(TypedDict, total=False):
    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[after], page[before], page[limit], page[size], page[number]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Page(TypedDict, total=False):
    """Consolidated page parameter (deepObject style).

    Originally: page[after], page[before], page[limit], page[size], page[number]
    """

    after: str
    """Opaque identifier of next page"""

    before: str
    """Opaque identifier of previous page"""

    limit: int
    """Limit of records per single page"""

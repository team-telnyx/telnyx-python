# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentListParams", "Filter", "FilterCreatedAt", "FilterCustomerReference", "FilterFilename", "Page"]


class DocumentListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for documents (deepObject style).

    Originally: filter[filename][contains], filter[customer_reference][eq],
    filter[customer_reference][in][], filter[created_at][gt], filter[created_at][lt]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: List[Literal["filename", "created_at", "updated_at", "-filename", "-created_at", "-updated_at"]]
    """Consolidated sort parameter for documents (deepObject style).

    Originally: sort[]
    """


class FilterCreatedAt(TypedDict, total=False):
    gt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by created at greater than provided value."""

    lt: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by created at less than provided value."""


_FilterCustomerReferenceReservedKeywords = TypedDict(
    "_FilterCustomerReferenceReservedKeywords",
    {
        "in": List[str],
    },
    total=False,
)


class FilterCustomerReference(_FilterCustomerReferenceReservedKeywords, total=False):
    eq: str
    """Filter documents by a customer reference."""


class FilterFilename(TypedDict, total=False):
    contains: str
    """Filter by string matching part of filename."""


class Filter(TypedDict, total=False):
    created_at: FilterCreatedAt

    customer_reference: FilterCustomerReference

    filename: FilterFilename


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

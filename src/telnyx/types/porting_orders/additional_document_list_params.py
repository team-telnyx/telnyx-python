# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["AdditionalDocumentListParams", "Filter", "Page", "Sort"]


class AdditionalDocumentListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[document_type]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: Sort
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""


class Filter(TypedDict, total=False):
    document_type: List[Literal["loa", "invoice", "csr", "other"]]
    """Filter additional documents by a list of document types"""


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

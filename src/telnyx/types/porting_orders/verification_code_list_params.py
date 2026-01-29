# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VerificationCodeListParams", "Filter", "Sort"]


class VerificationCodeListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style). Originally: filter[verified]"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Sort
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style). Originally: filter[verified]"""

    verified: bool
    """Filter verification codes that have been verified or not"""


class Sort(TypedDict, total=False):
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""

    value: Literal["created_at", "-created_at"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """

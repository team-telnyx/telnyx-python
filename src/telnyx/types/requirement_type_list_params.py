# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["RequirementTypeListParams", "Filter", "FilterName"]


class RequirementTypeListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for requirement types (deepObject style).

    Originally: filter[name]
    """

    sort: List[Literal["name", "created_at", "updated_at", "-name", "-created_at", "-updated_at"]]
    """Consolidated sort parameter for requirement types (deepObject style).

    Originally: sort[]
    """


class FilterName(TypedDict, total=False):
    contains: str
    """Filters requirement types to those whose name contains a certain string."""


class Filter(TypedDict, total=False):
    name: FilterName

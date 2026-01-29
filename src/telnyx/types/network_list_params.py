# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NetworkListParams", "Filter"]


class NetworkListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style). Originally: filter[name]"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style). Originally: filter[name]"""

    name: str
    """The network name to filter on."""

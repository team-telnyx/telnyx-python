# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReportListParams", "Filter"]


class ReportListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[report_type], filter[status]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[report_type], filter[status]
    """

    report_type: Literal["export_porting_orders_csv"]
    """Filter reports of a specific type"""

    status: Literal["pending", "completed"]
    """Filter reports of a specific status"""

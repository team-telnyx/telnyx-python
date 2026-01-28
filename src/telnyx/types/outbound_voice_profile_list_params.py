# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OutboundVoiceProfileListParams", "Filter", "FilterName"]


class OutboundVoiceProfileListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[name][contains]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Literal[
        "enabled",
        "-enabled",
        "created_at",
        "-created_at",
        "name",
        "-name",
        "service_plan",
        "-service_plan",
        "traffic_type",
        "-traffic_type",
        "usage_payment_method",
        "-usage_payment_method",
    ]
    """Specifies the sort order for results.

    By default sorting direction is ascending. To have the results sorted in
    descending order add the <code>-</code> prefix.<br/><br/> That is: <ul>

      <li>
        <code>name</code>: sorts the result by the
        <code>name</code> field in ascending order.
      </li>

      <li>
        <code>-name</code>: sorts the result by the
        <code>name</code> field in descending order.
      </li>
    </ul> <br/>
    """


class FilterName(TypedDict, total=False):
    """Name filtering operations"""

    contains: str
    """Optional filter on outbound voice profile name."""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[name][contains]
    """

    name: FilterName
    """Name filtering operations"""

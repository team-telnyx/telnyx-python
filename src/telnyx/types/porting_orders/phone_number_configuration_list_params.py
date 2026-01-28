# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PhoneNumberConfigurationListParams", "Filter", "FilterPortingOrder", "Sort"]


class PhoneNumberConfigurationListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[porting_order.status][in][],
    filter[porting_phone_number][in][], filter[user_bundle_id][in][]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Sort
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""


class FilterPortingOrder(TypedDict, total=False):
    status: List[
        Literal[
            "activation-in-progress",
            "cancel-pending",
            "cancelled",
            "draft",
            "exception",
            "foc-date-confirmed",
            "in-process",
            "ported",
            "submitted",
        ]
    ]
    """Filter results by specific porting order statuses"""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[porting_order.status][in][], filter[porting_phone_number][in][], filter[user_bundle_id][in][]
    """

    porting_order: FilterPortingOrder

    porting_phone_number: SequenceNotStr[str]
    """Filter results by a list of porting phone number IDs"""

    user_bundle_id: SequenceNotStr[str]
    """Filter results by a list of user bundle IDs"""


class Sort(TypedDict, total=False):
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""

    value: Literal["created_at", "-created_at"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """

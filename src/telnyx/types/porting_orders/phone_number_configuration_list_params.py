# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PhoneNumberConfigurationListParams", "Filter", "Page", "Sort"]


class PhoneNumberConfigurationListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[porting_order.status][in][],
    filter[porting_phone_number][in][], filter[user_bundle_id][in][]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: Sort
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""


class Filter(TypedDict, total=False):
    porting_order_status: Annotated[
        List[
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
        ],
        PropertyInfo(alias="porting_order.status"),
    ]
    """Filter results by specific porting order statuses"""

    porting_phone_number: List[str]
    """Filter results by a list of porting phone number IDs"""

    user_bundle_id: List[str]
    """Filter results by a list of user bundle IDs"""


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

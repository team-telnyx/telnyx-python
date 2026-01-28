# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PhoneNumberBlockListParams", "Filter", "Sort"]


class PhoneNumberBlockListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[porting_order_id], filter[support_key], filter[status],
    filter[phone_number], filter[activation_status], filter[portability_status]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Sort
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[porting_order_id], filter[support_key], filter[status], filter[phone_number], filter[activation_status], filter[portability_status]
    """

    activation_status: Literal[
        "New",
        "Pending",
        "Conflict",
        "Cancel Pending",
        "Failed",
        "Concurred",
        "Activate RDY",
        "Disconnect Pending",
        "Concurrence Sent",
        "Old",
        "Sending",
        "Active",
        "Cancelled",
    ]
    """Filter results by activation status"""

    phone_number: SequenceNotStr[str]
    """Filter results by a list of phone numbers"""

    portability_status: Literal["pending", "confirmed", "provisional"]
    """Filter results by portability status"""

    porting_order_id: SequenceNotStr[str]
    """Filter results by a list of porting order ids"""

    status: Union[
        Literal[
            "draft",
            "in-process",
            "submitted",
            "exception",
            "foc-date-confirmed",
            "cancel-pending",
            "ported",
            "cancelled",
        ],
        List[
            Literal[
                "draft",
                "in-process",
                "submitted",
                "exception",
                "foc-date-confirmed",
                "cancel-pending",
                "ported",
                "cancelled",
            ]
        ],
    ]
    """Filter porting orders by status(es).

    Originally: filter[status], filter[status][in][]
    """

    support_key: Union[str, SequenceNotStr[str]]
    """Filter results by support key(s).

    Originally: filter[support_key][eq], filter[support_key][in][]
    """


class Sort(TypedDict, total=False):
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""

    value: Literal["-created_at", "created_at"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order
    """

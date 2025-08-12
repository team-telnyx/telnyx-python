# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

__all__ = [
    "GlobalIPAssignmentHealthRetrieveParams",
    "Filter",
    "FilterGlobalIPAssignmentID",
    "FilterGlobalIPAssignmentIDIn",
    "FilterGlobalIPID",
    "FilterGlobalIPIDIn",
]


class GlobalIPAssignmentHealthRetrieveParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[global_ip_id][in], filter[global_ip_assignment_id][in]
    """


_FilterGlobalIPAssignmentIDInReservedKeywords = TypedDict(
    "_FilterGlobalIPAssignmentIDInReservedKeywords",
    {
        "in": str,
    },
    total=False,
)


class FilterGlobalIPAssignmentIDIn(_FilterGlobalIPAssignmentIDInReservedKeywords, total=False):
    pass


FilterGlobalIPAssignmentID: TypeAlias = Union[str, FilterGlobalIPAssignmentIDIn]

_FilterGlobalIpidInReservedKeywords = TypedDict(
    "_FilterGlobalIpidInReservedKeywords",
    {
        "in": str,
    },
    total=False,
)


class FilterGlobalIPIDIn(_FilterGlobalIpidInReservedKeywords, total=False):
    pass


FilterGlobalIPID: TypeAlias = Union[str, FilterGlobalIPIDIn]


class Filter(TypedDict, total=False):
    global_ip_assignment_id: FilterGlobalIPAssignmentID
    """Filter by exact Global IP Assignment ID"""

    global_ip_id: FilterGlobalIPID
    """Filter by exact Global IP ID"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TelephonyCredentialListParams", "Filter"]


class TelephonyCredentialListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[tag], filter[name], filter[status], filter[resource_id],
    filter[sip_username]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[tag], filter[name], filter[status], filter[resource_id], filter[sip_username]
    """

    name: str
    """Filter by name"""

    resource_id: str
    """Filter by resource_id"""

    sip_username: str
    """Filter by sip_username"""

    status: str
    """Filter by status"""

    tag: str
    """Filter by tag"""

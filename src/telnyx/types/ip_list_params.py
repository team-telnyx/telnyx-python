# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IPListParams", "Filter"]


class IPListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[connection_id], filter[ip_address], filter[port]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[connection_id], filter[ip_address], filter[port]
    """

    connection_id: str
    """ID of the IP Connection to which this IP should be attached."""

    ip_address: str
    """IP adddress represented by this resource."""

    port: int
    """Port to use when connecting to this IP."""

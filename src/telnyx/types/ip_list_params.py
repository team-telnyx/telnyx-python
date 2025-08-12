# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IPListParams", "Filter", "Page"]


class IPListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[connection_id], filter[ip_address], filter[port]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class Filter(TypedDict, total=False):
    connection_id: str
    """ID of the IP Connection to which this IP should be attached."""

    ip_address: str
    """IP adddress represented by this resource."""

    port: int
    """Port to use when connecting to this IP."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

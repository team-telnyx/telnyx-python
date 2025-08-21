# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TelephonyCredentialListParams", "Filter", "Page"]


class TelephonyCredentialListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[tag], filter[name], filter[status], filter[resource_id],
    filter[sip_username]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """


class Filter(TypedDict, total=False):
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


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

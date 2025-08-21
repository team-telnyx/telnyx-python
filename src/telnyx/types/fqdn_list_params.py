# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FqdnListParams", "Filter", "Page"]


class FqdnListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[connection_id], filter[fqdn], filter[port],
    filter[dns_record_type]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class Filter(TypedDict, total=False):
    connection_id: str
    """ID of the FQDN connection to which the FQDN belongs."""

    dns_record_type: str
    """DNS record type used by the FQDN."""

    fqdn: str
    """FQDN represented by the resource."""

    port: int
    """Port to use when connecting to the FQDN."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

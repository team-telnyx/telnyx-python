# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LogMessageListParams", "Filter", "FilterTelephoneNumber", "Page"]


class LogMessageListParams(TypedDict, total=False):
    filter: Filter
    """Filter parameter for log messages (deepObject style).

    Supports filtering by external_connection_id and telephone_number with
    eq/contains operations.
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class FilterTelephoneNumber(TypedDict, total=False):
    contains: str
    """The partial phone number to filter log messages for. Requires 3-15 digits."""

    eq: str
    """
    The phone number to filter log messages for or "null" to filter for logs without
    a phone number
    """


class Filter(TypedDict, total=False):
    external_connection_id: str
    """
    The external connection ID to filter by or "null" to filter for logs without an
    external connection ID
    """

    telephone_number: FilterTelephoneNumber
    """Telephone number filter operations for log messages.

    Use 'eq' for exact matches or 'contains' for partial matches.
    """


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VoiceListParams", "Filter", "FilterConnectionName", "Page"]


class VoiceListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[phone_number], filter[connection_name],
    filter[customer_reference], filter[voice.usage_payment_method]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: Literal["purchased_at", "phone_number", "connection_name", "usage_payment_method"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """


class FilterConnectionName(TypedDict, total=False):
    contains: str
    """Filter contains connection name. Requires at least three characters."""


class Filter(TypedDict, total=False):
    connection_name: FilterConnectionName
    """Filter by connection name pattern matching."""

    customer_reference: str
    """Filter numbers via the customer_reference set."""

    phone_number: str
    """Filter by phone number.

    Requires at least three digits. Non-numerical characters will result in no
    values being returned.
    """

    voice_usage_payment_method: Annotated[
        Literal["pay-per-minute", "channel"], PropertyInfo(alias="voice.usage_payment_method")
    ]
    """Filter by usage_payment_method."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""

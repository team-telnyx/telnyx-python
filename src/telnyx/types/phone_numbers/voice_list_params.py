# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VoiceListParams", "Filter", "FilterConnectionName"]


class VoiceListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[phone_number], filter[connection_name],
    filter[customer_reference], filter[voice.usage_payment_method]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Literal["purchased_at", "phone_number", "connection_name", "usage_payment_method"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """


class FilterConnectionName(TypedDict, total=False):
    """Filter by connection name pattern matching."""

    contains: str
    """Filter contains connection name. Requires at least three characters."""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[phone_number], filter[connection_name], filter[customer_reference], filter[voice.usage_payment_method]
    """

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

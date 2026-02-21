# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessagingHostedNumberListParams"]


class MessagingHostedNumberListParams(TypedDict, total=False):
    filter_messaging_profile_id: Annotated[str, PropertyInfo(alias="filter[messaging_profile_id]")]
    """Filter by messaging profile ID."""

    filter_phone_number: Annotated[str, PropertyInfo(alias="filter[phone_number]")]
    """Filter by exact phone number."""

    filter_phone_number_contains: Annotated[str, PropertyInfo(alias="filter[phone_number][contains]")]
    """Filter by phone number substring."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort_phone_number: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sort[phone_number]")]
    """Sort by phone number."""

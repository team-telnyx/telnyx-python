# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AlphanumericSenderIDListParams"]


class AlphanumericSenderIDListParams(TypedDict, total=False):
    filter_messaging_profile_id: Annotated[str, PropertyInfo(alias="filter[messaging_profile_id]")]
    """Filter by messaging profile ID."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Page size."""

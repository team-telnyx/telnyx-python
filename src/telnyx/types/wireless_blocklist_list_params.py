# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WirelessBlocklistListParams"]


class WirelessBlocklistListParams(TypedDict, total=False):
    filter_name: Annotated[str, PropertyInfo(alias="filter[name]")]
    """The name of the Wireless Blocklist."""

    filter_type: Annotated[str, PropertyInfo(alias="filter[type]")]
    """When the Private Wireless Gateway was last updated."""

    filter_values: Annotated[str, PropertyInfo(alias="filter[values]")]
    """Values to filter on (inclusive)."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page number to load."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """The size of the page."""

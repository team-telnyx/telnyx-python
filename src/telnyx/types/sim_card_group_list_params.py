# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimCardGroupListParams"]


class SimCardGroupListParams(TypedDict, total=False):
    filter_name: Annotated[str, PropertyInfo(alias="filter[name]")]
    """A valid SIM card group name."""

    filter_private_wireless_gateway_id: Annotated[str, PropertyInfo(alias="filter[private_wireless_gateway_id]")]
    """A Private Wireless Gateway ID associated with the group."""

    filter_wireless_blocklist_id: Annotated[str, PropertyInfo(alias="filter[wireless_blocklist_id]")]
    """A Wireless Blocklist ID associated with the group."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page number to load."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """The size of the page."""

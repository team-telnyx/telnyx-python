# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PrivateWirelessGatewayListParams"]


class PrivateWirelessGatewayListParams(TypedDict, total=False):
    filter_created_at: Annotated[str, PropertyInfo(alias="filter[created_at]")]
    """Private Wireless Gateway resource creation date."""

    filter_ip_range: Annotated[str, PropertyInfo(alias="filter[ip_range]")]
    """The IP address range of the Private Wireless Gateway."""

    filter_name: Annotated[str, PropertyInfo(alias="filter[name]")]
    """The name of the Private Wireless Gateway."""

    filter_region_code: Annotated[str, PropertyInfo(alias="filter[region_code]")]
    """The name of the region where the Private Wireless Gateway is deployed."""

    filter_updated_at: Annotated[str, PropertyInfo(alias="filter[updated_at]")]
    """When the Private Wireless Gateway was last updated."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page number to load."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """The size of the page."""

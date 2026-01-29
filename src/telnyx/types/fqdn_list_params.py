# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FqdnListParams", "Filter"]


class FqdnListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[connection_id], filter[fqdn], filter[port],
    filter[dns_record_type]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[connection_id], filter[fqdn], filter[port], filter[dns_record_type]
    """

    connection_id: str
    """ID of the FQDN connection to which the FQDN belongs."""

    dns_record_type: str
    """DNS record type used by the FQDN."""

    fqdn: str
    """FQDN represented by the resource."""

    port: int
    """Port to use when connecting to the FQDN."""

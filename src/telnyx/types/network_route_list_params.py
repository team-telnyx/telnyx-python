# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NetworkRouteListParams", "Filter", "Page"]


class NetworkRouteListParams(TypedDict, total=False):
    filter: Required[Filter]
    """Consolidated filter parameter (deepObject style).

    Originally: filter[network_id], filter[origin], filter[next_hop.type],
    filter[cidr], filter[status]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[after], page[limit]
    """

    sort: Literal["cidr", "-cidr", "status", "-status", "created_at", "-created_at"]
    """Sorts the results by a field, ascending, or descending with a leading `-`.

    The default is `-created_at`.
    """


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[network_id], filter[origin], filter[next_hop.type], filter[cidr], filter[status]
    """

    network_id: Required[str]
    """The id of the Network whose route table is returned. Required."""

    cidr: str
    """Only routes with this CIDR."""

    next_hop_type: Annotated[
        Literal[
            "tunnel",
            "wireguard_peer",
            "wireguard_interface",
            "private_wireless_gateway",
            "virtual_cross_connect",
            "ipsec_tunnel",
            "public_internet_gateway",
        ],
        PropertyInfo(alias="next_hop.type"),
    ]
    """Only routes whose next hop has this type."""

    origin: Literal["static", "attachment"]
    """Only routes of this origin."""

    status: Literal["pending", "active", "inactive", "failed"]
    """Only routes with this status."""


class Page(TypedDict, total=False):
    """Consolidated page parameter (deepObject style).

    Originally: page[after], page[limit]
    """

    after: str
    """The cursor from `meta.cursors.after` of the previous page."""

    limit: int
    """The number of results per page."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NetworkRouteCreateParams", "NextHop"]


class NetworkRouteCreateParams(TypedDict, total=False):
    cidr: Required[str]
    """The IPv4 subnet to route, such as a subnet behind the tunnel.

    It must be a canonical CIDR. Default, loopback, link-local, multicast, and
    shared address space (`100.64.0.0/10`) ranges are rejected. So are ranges that
    overlap the Tailscale Subnet Router ranges, `172.27.254.0/24` and
    `198.18.0.0/20`, or a subnet already on the Network.
    """

    network_id: Required[str]
    """The id of the Network to add the route to."""

    next_hop: Required[NextHop]
    """Where the Network sends traffic for `cidr`."""


class NextHop(TypedDict, total=False):
    """Where the Network sends traffic for `cidr`."""

    id: Required[str]
    """The id of the tunnel."""

    type: Required[Literal["tunnel"]]
    """The type of the next hop."""

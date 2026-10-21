# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["TailscaleSubnetRouterCreateParams"]


class TailscaleSubnetRouterCreateParams(TypedDict, total=False):
    advertised_routes: Required[SequenceNotStr[str]]
    """IPv4 subnets of the Network that the router advertises to the tailnet.

    Each entry is a canonical CIDR that the Network routes. Default, loopback,
    link-local, multicast, and Tailscale (`100.64.0.0/10`) ranges are rejected. So
    are ranges that overlap the router's own, `172.27.254.0/24` and `198.18.0.0/20`.
    """

    auth_key: Required[str]
    """
    A Tailscale auth key that enrolls the router in the user's tailnet: reusable,
    pre-approved, tagged, and not ephemeral. Telnyx stores it encrypted until
    enrollment succeeds, then discards it. It is never returned.
    """

    name: Required[str]
    """A user specified name for the router."""

    network_id: Required[str]
    """The id of the Network to attach the router to."""

    region_code: Required[str]
    """The code of the region to create the router in.

    `GET /network_coverage` lists the regions whose `available_services` include
    `tailscale_subnet_router`.
    """

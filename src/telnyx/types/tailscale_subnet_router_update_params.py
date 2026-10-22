# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["TailscaleSubnetRouterUpdateParams"]


class TailscaleSubnetRouterUpdateParams(TypedDict, total=False):
    advertised_routes: SequenceNotStr[str]
    """IPv4 subnets of the Network that the router advertises to the tailnet.

    Each entry is a canonical CIDR that the Network routes. Default, loopback,
    link-local, multicast, and Tailscale (`100.64.0.0/10`) ranges are rejected. So
    are ranges that overlap the router's own, `172.27.254.0/24` and `198.18.0.0/20`.
    """

    auth_key: str
    """A replacement Tailscale auth key.

    Accepted only while the router has never enrolled, for example after a `failed`
    enrollment. Never returned.
    """

    name: str
    """A user specified name for the router."""

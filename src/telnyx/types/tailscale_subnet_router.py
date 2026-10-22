# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TailscaleSubnetRouter"]


class TailscaleSubnetRouter(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    advertised_routes: Optional[List[str]] = None
    """IPv4 subnets of the Network that the router advertises to the tailnet.

    Each entry is a canonical CIDR that the Network routes. Default, loopback,
    link-local, multicast, and Tailscale (`100.64.0.0/10`) ranges are rejected. So
    are ranges that overlap the router's own, `172.27.254.0/24` and `198.18.0.0/20`.
    """

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    customer_address: Optional[str] = None
    """The router's address on the Network, from `172.27.254.0/24`.

    Tailnet traffic enters the Network from this address.
    """

    device_id: Optional[str] = None
    """The router's node id on the tailnet. Set once the router has enrolled."""

    name: Optional[str] = None
    """A user specified name for the router."""

    network_id: Optional[str] = None
    """The id of the Network the router is attached to."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    region_code: Optional[str] = None
    """The code of the region the router is created in.

    `GET /network_coverage` lists the regions whose `available_services` include
    `tailscale_subnet_router`.
    """

    status: Optional[Literal["provisioning", "provisioned", "failed", "deleting"]] = None
    """`provisioning`: Telnyx is creating the router or applying a change.

    `provisioned`: the router is on the tailnet and advertises its routes; the
    tailnet still approves them. `failed`: enrollment did not complete, and `PATCH`
    retries it. `deleting`: the router is being removed.
    """

    tailnet_name: Optional[str] = None
    """The name of the tailnet the router is enrolled in.

    Set once the router has enrolled.
    """

    tailscale_ips: Optional[List[str]] = None
    """The router's addresses on the tailnet. Empty until the router has enrolled."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""

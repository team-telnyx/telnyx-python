# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NetworkRoute", "NextHop"]


class NextHop(BaseModel):
    """Where the Network sends traffic for the route's CIDR."""

    id: str
    """The id of the tunnel or attachment."""

    type: Literal[
        "tunnel",
        "wireguard_peer",
        "wireguard_interface",
        "private_wireless_gateway",
        "virtual_cross_connect",
        "ipsec_tunnel",
        "public_internet_gateway",
    ]
    """The type of the next hop.

    Routes added with `POST /network_routes` use `tunnel`. Routes that attachments
    install carry the attachment's type.
    """


class NetworkRoute(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    cidr: Optional[str] = None
    """The IPv4 CIDR the route covers."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    network_id: Optional[str] = None
    """The id of the Network the route belongs to."""

    next_hop: Optional[NextHop] = None
    """Where the Network sends traffic for the route's CIDR."""

    origin: Optional[Literal["static", "attachment"]] = None
    """
    `static` for a route added with `POST /network_routes`, `attachment` for a route
    that another resource installed and removes.
    """

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    status: Optional[Literal["pending", "active", "inactive", "failed"]] = None
    """`pending` until Telnyx installs the route on the Network, then `active`.

    `inactive` while a tunnel next hop has no connected process. `failed` (Preview,
    not reported yet) when Telnyx could not install the route.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgentGateway"]


class AgentGateway(BaseModel):
    """An Agent Gateway instance on a WireGuard Interface."""

    id: str
    """Identifies the instance."""

    created_at: datetime
    """When the instance was created."""

    engine: Literal["litellm"]
    """The gateway engine."""

    engine_version: str
    """The engine version the instance runs."""

    gateway_url: Optional[str] = None
    """
    The base URL of the instance's API, `http://<address>:4000`, where the address
    is the instance's peer address on the WireGuard Interface. Reachable only from
    hosts on the instance's _Network_, and every request to it carries a key from
    this API. `null` until the instance is `ready`.
    """

    name: Optional[str] = None
    """A label for people; `null` when none was given."""

    network_id: Optional[str] = None
    """
    The [_Network_](https://developers.telnyx.com/docs/network/overview) the
    WireGuard Interface belongs to.
    """

    status: Literal["pending", "provisioning", "ready", "failed", "deleting"]
    """Where the instance is in its lifecycle.

    `pending`: created and waiting to start. `provisioning`: starting. `ready`:
    running, with its `gateway_url` set. `failed`: did not start in time; delete it.
    `deleting`: being removed.
    """

    wireguard_interface_id: Optional[str] = None
    """The WireGuard Interface the instance joins as a peer."""

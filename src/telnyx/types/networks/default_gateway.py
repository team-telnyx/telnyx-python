# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..record import Record
from ..interface_status import InterfaceStatus

__all__ = ["DefaultGateway"]


class DefaultGateway(Record):
    network_id: Optional[str] = None
    """Network ID."""

    status: Optional[InterfaceStatus] = None
    """The current status of the interface deployment."""

    wireguard_peer_id: Optional[str] = None
    """Wireguard peer ID."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .record import Record
from .interface_status import InterfaceStatus

__all__ = ["GlobalIPAssignment"]


class GlobalIPAssignment(Record):
    global_ip_id: Optional[str] = None
    """Global IP ID."""

    is_announced: Optional[bool] = None
    """Status of BGP announcement."""

    is_connected: Optional[bool] = None
    """Wireguard peer is connected."""

    is_in_maintenance: Optional[bool] = None
    """Enable/disable BGP announcement."""

    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""

    status: Optional[InterfaceStatus] = None
    """The current status of the interface deployment."""

    wireguard_peer_id: Optional[str] = None
    """Wireguard peer ID."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GlobalIPAssignmentCreateParams"]


class GlobalIPAssignmentCreateParams(TypedDict, total=False):
    global_ip_id: str
    """Global IP ID."""

    is_in_maintenance: bool
    """Enable/disable BGP announcement."""

    wireguard_peer_id: str
    """Wireguard peer ID."""

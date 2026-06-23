# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .record_param import RecordParam

__all__ = ["WireguardPeerParam"]


class WireguardPeerParam(RecordParam, total=False):
    wireguard_interface_id: str
    """The id of the wireguard interface associated with the peer."""

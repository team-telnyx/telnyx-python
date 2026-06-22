# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .record_param import RecordParam
from .network_interface_param import NetworkInterfaceParam

__all__ = ["WireguardInterfaceParam"]


class WireguardInterfaceParam(RecordParam, NetworkInterfaceParam, total=False):
    enable_sip_trunking: bool
    """Enable SIP traffic forwarding over VPN interface."""

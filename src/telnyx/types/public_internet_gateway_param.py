# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .record_param import RecordParam
from .network_interface_param import NetworkInterfaceParam

__all__ = ["PublicInternetGatewayParam"]


class PublicInternetGatewayParam(RecordParam, NetworkInterfaceParam, total=False):
    region_code: str
    """The region interface is deployed to."""

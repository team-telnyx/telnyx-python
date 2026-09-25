# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .wireless_private_wireless_gateway import WirelessPrivateWirelessGateway

__all__ = ["PrivateWirelessGatewayCreateResponse"]


class PrivateWirelessGatewayCreateResponse(BaseModel):
    data: Optional[WirelessPrivateWirelessGateway] = None

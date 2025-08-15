# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .private_wireless_gateway import PrivateWirelessGateway

__all__ = ["PrivateWirelessGatewayDeleteResponse"]


class PrivateWirelessGatewayDeleteResponse(BaseModel):
    data: Optional[PrivateWirelessGateway] = None

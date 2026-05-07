# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .wireguard_interface_read import WireguardInterfaceRead

__all__ = ["WireguardInterfaceCreateResponse"]


class WireguardInterfaceCreateResponse(BaseModel):
    data: Optional[WireguardInterfaceRead] = None

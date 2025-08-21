# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .wireless_blocklist import WirelessBlocklist

__all__ = ["WirelessBlocklistDeleteResponse"]


class WirelessBlocklistDeleteResponse(BaseModel):
    data: Optional[WirelessBlocklist] = None

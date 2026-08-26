# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .wireless_wireless_blocklist import WirelessWirelessBlocklist

__all__ = ["WirelessBlocklistCreateResponse"]


class WirelessBlocklistCreateResponse(BaseModel):
    data: Optional[WirelessWirelessBlocklist] = None

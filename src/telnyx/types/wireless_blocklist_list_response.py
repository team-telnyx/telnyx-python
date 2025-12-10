# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .wireless_blocklist import WirelessBlocklist

__all__ = ["WirelessBlocklistListResponse"]


class WirelessBlocklistListResponse(BaseModel):
    data: Optional[List[WirelessBlocklist]] = None

    meta: Optional[PaginationMeta] = None

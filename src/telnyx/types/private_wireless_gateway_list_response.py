# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .private_wireless_gateway import PrivateWirelessGateway

__all__ = ["PrivateWirelessGatewayListResponse"]


class PrivateWirelessGatewayListResponse(BaseModel):
    data: Optional[List[PrivateWirelessGateway]] = None

    meta: Optional[PaginationMeta] = None

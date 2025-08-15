# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .ip_connection import IPConnection
from .shared.connections_pagination_meta import ConnectionsPaginationMeta

__all__ = ["IPConnectionListResponse"]


class IPConnectionListResponse(BaseModel):
    data: Optional[List[IPConnection]] = None

    meta: Optional[ConnectionsPaginationMeta] = None

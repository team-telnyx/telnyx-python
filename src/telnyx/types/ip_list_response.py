# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .ip import IP
from .._models import BaseModel
from .shared.connections_pagination_meta import ConnectionsPaginationMeta

__all__ = ["IPListResponse"]


class IPListResponse(BaseModel):
    data: Optional[List[IP]] = None

    meta: Optional[ConnectionsPaginationMeta] = None

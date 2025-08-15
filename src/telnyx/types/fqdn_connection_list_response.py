# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .fqdn_connection import FqdnConnection
from .shared.connections_pagination_meta import ConnectionsPaginationMeta

__all__ = ["FqdnConnectionListResponse"]


class FqdnConnectionListResponse(BaseModel):
    data: Optional[List[FqdnConnection]] = None

    meta: Optional[ConnectionsPaginationMeta] = None

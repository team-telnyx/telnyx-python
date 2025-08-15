# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .fqdn import Fqdn
from .._models import BaseModel
from .shared.connections_pagination_meta import ConnectionsPaginationMeta

__all__ = ["FqdnListResponse"]


class FqdnListResponse(BaseModel):
    data: Optional[List[Fqdn]] = None

    meta: Optional[ConnectionsPaginationMeta] = None

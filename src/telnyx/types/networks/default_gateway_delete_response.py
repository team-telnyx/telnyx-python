# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .default_gateway import DefaultGateway
from ..pagination_meta import PaginationMeta

__all__ = ["DefaultGatewayDeleteResponse"]


class DefaultGatewayDeleteResponse(BaseModel):
    data: Optional[List[DefaultGateway]] = None

    meta: Optional[PaginationMeta] = None

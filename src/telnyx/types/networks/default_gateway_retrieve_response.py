# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ..._models import BaseModel
from .default_gateway import DefaultGateway

if TYPE_CHECKING:
    from ..pagination_meta import PaginationMeta

__all__ = ["DefaultGatewayRetrieveResponse"]


class DefaultGatewayRetrieveResponse(BaseModel):
    data: Optional[List[DefaultGateway]] = None

    meta: Optional[PaginationMeta] = None

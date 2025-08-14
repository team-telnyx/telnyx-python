# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .migration_params import MigrationParams
from .buckets.pagination_meta_simple import PaginationMetaSimple

__all__ = ["MigrationListResponse"]


class MigrationListResponse(BaseModel):
    data: Optional[List[MigrationParams]] = None

    meta: Optional[PaginationMetaSimple] = None

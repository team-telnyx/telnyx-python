# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .migration_source_params import MigrationSourceParams
from .buckets.pagination_meta_simple import PaginationMetaSimple

__all__ = ["MigrationSourceListResponse"]


class MigrationSourceListResponse(BaseModel):
    data: Optional[List[MigrationSourceParams]] = None

    meta: Optional[PaginationMetaSimple] = None

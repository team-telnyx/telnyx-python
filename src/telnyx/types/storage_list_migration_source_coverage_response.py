# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .storage.buckets.pagination_meta_simple import PaginationMetaSimple

__all__ = ["StorageListMigrationSourceCoverageResponse", "Data"]


class Data(BaseModel):
    provider: Optional[Literal["aws"]] = None
    """Cloud provider from which to migrate data."""

    source_region: Optional[str] = None
    """Provider region from which to migrate data."""


class StorageListMigrationSourceCoverageResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMetaSimple] = None

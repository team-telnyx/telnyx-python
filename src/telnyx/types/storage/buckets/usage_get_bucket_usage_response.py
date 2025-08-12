# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from .pagination_meta_simple import PaginationMetaSimple

__all__ = ["UsageGetBucketUsageResponse", "Data"]


class Data(BaseModel):
    num_objects: Optional[int] = None
    """The number of objects in the bucket"""

    size: Optional[int] = None
    """The size of the bucket in bytes"""

    size_kb: Optional[int] = None
    """The size of the bucket in kilobytes"""

    timestamp: Optional[datetime] = None
    """The time the snapshot was taken"""


class UsageGetBucketUsageResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMetaSimple] = None

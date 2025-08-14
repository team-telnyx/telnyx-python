# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["UsageGetAPIUsageResponse", "Data", "DataCategory", "DataTotal"]


class DataCategory(BaseModel):
    bytes_received: Optional[int] = None
    """The number of bytes received"""

    bytes_sent: Optional[int] = None
    """The number of bytes sent"""

    category: Optional[
        Literal[
            "list_bucket",
            "list_buckets",
            "get-bucket_location",
            "create_bucket",
            "stat_bucket",
            "get_bucket_versioning",
            "set_bucket_versioning",
            "get_obj",
            "put_obj",
            "delete_obj",
        ]
    ] = None
    """The category of the bucket operation"""

    ops: Optional[int] = None
    """The number of operations"""

    successful_ops: Optional[int] = None
    """The number of successful operations"""


class DataTotal(BaseModel):
    bytes_received: Optional[int] = None
    """The number of bytes received"""

    bytes_sent: Optional[int] = None
    """The number of bytes sent"""

    ops: Optional[int] = None
    """The number of operations"""

    successful_ops: Optional[int] = None
    """The number of successful operations"""


class Data(BaseModel):
    categories: Optional[List[DataCategory]] = None

    timestamp: Optional[datetime] = None
    """The time the usage was recorded"""

    total: Optional[DataTotal] = None


class UsageGetAPIUsageResponse(BaseModel):
    data: Optional[List[Data]] = None

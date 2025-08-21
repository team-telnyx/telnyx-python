# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .record import Record
from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["GlobalIPHealthCheckListResponse", "Data"]


class Data(Record):
    global_ip_id: Optional[str] = None
    """Global IP ID."""

    health_check_params: Optional[Dict[str, object]] = None
    """A Global IP health check params."""

    health_check_type: Optional[str] = None
    """The Global IP health check type."""

    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""


class GlobalIPHealthCheckListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

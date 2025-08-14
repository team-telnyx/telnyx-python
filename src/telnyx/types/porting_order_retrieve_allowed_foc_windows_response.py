# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["PortingOrderRetrieveAllowedFocWindowsResponse", "Data"]


class Data(BaseModel):
    ended_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating the end of the range of foc window"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    started_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating the start of the range of foc window."""


class PortingOrderRetrieveAllowedFocWindowsResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

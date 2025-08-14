# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["ShortCodeListResponse", "Data"]


class Data(BaseModel):
    messaging_profile_id: Optional[str] = None
    """Unique identifier for a messaging profile."""

    id: Optional[str] = None
    """Identifies the type of resource."""

    country_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    record_type: Optional[Literal["short_code"]] = None
    """Identifies the type of the resource."""

    short_code: Optional[str] = None
    """Short digit sequence used to address messages."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class ShortCodeListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

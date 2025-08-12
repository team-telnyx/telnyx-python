# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .available_service import AvailableService

__all__ = ["NetworkCoverageListResponse", "Data", "DataLocation"]


class DataLocation(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the resource."""

    additional_info: Optional[str] = None

    description: Optional[str] = None

    is_default: Optional[bool] = None
    """Represents whether the location is the default or not."""


class Data(BaseModel):
    available_services: Optional[List[AvailableService]] = None
    """List of interface types supported in this region."""

    location: Optional[DataLocation] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class NetworkCoverageListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

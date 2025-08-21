# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["ListRetrieveByZoneResponse", "Data", "DataNumber"]


class DataNumber(BaseModel):
    country: Optional[str] = None

    number: Optional[str] = None


class Data(BaseModel):
    number_of_channels: Optional[int] = None

    numbers: Optional[List[DataNumber]] = None

    zone_id: Optional[str] = None

    zone_name: Optional[str] = None


class ListRetrieveByZoneResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

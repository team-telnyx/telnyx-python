# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InventoryCoverageListResponse", "Data", "Meta"]


class Data(BaseModel):
    administrative_area: Optional[str] = None

    advance_requirements: Optional[bool] = None
    """Indicates if the phone number requires advance requirements."""

    count: Optional[int] = None

    coverage_type: Optional[Literal["number", "block"]] = None

    group: Optional[str] = None

    group_type: Optional[str] = None

    number_range: Optional[int] = None

    number_type: Optional[Literal["did", "toll-free"]] = None

    phone_number_type: Optional[Literal["local", "toll_free", "national", "landline", "shared_cost", "mobile"]] = None

    record_type: Optional[str] = None


class Meta(BaseModel):
    total_results: Optional[int] = None


class InventoryCoverageListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None

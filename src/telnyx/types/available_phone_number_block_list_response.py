# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "AvailablePhoneNumberBlockListResponse",
    "Data",
    "DataCostInformation",
    "DataFeature",
    "DataRegionInformation",
    "Meta",
]


class DataCostInformation(BaseModel):
    currency: Optional[str] = None
    """The ISO 4217 code for the currency."""

    monthly_cost: Optional[str] = None

    upfront_cost: Optional[str] = None


class DataFeature(BaseModel):
    name: Optional[str] = None


class DataRegionInformation(BaseModel):
    region_name: Optional[str] = None

    region_type: Optional[Literal["country_code", "rate_center", "state", "location"]] = None


class Data(BaseModel):
    cost_information: Optional[DataCostInformation] = None

    features: Optional[List[DataFeature]] = None

    range: Optional[int] = None

    record_type: Optional[Literal["available_phone_number_block"]] = None

    region_information: Optional[List[DataRegionInformation]] = None

    starting_number: Optional[str] = None


class Meta(BaseModel):
    best_effort_results: Optional[int] = None

    total_results: Optional[int] = None


class AvailablePhoneNumberBlockListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None

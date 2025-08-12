# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "AvailablePhoneNumberListResponse",
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
    best_effort: Optional[bool] = None
    """
    Specifies whether the phone number is an exact match based on the search
    criteria or not.
    """

    cost_information: Optional[DataCostInformation] = None

    features: Optional[List[DataFeature]] = None

    phone_number: Optional[str] = None

    quickship: Optional[bool] = None
    """
    Specifies whether the phone number can receive calls immediately after purchase
    or not.
    """

    record_type: Optional[Literal["available_phone_number"]] = None

    region_information: Optional[List[DataRegionInformation]] = None

    reservable: Optional[bool] = None
    """Specifies whether the phone number can be reserved before purchase or not."""

    vanity_format: Optional[str] = None


class Meta(BaseModel):
    best_effort_results: Optional[int] = None

    total_results: Optional[int] = None


class AvailablePhoneNumberListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None

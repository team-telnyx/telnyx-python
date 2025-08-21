# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CivicAddressListResponse", "Data", "DataLocation"]


class DataLocation(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the resource."""

    additional_info: Optional[str] = None

    description: Optional[str] = None

    is_default: Optional[bool] = None
    """Represents whether the location is the default or not."""


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the resource."""

    city_or_town: Optional[str] = None

    city_or_town_alias: Optional[str] = None

    company_name: Optional[str] = None

    country: Optional[str] = None

    country_or_district: Optional[str] = None

    default_location_id: Optional[str] = None
    """Identifies what is the default location in the list of locations."""

    description: Optional[str] = None

    house_number: Optional[str] = None

    house_number_suffix: Optional[str] = None

    locations: Optional[List[DataLocation]] = None

    postal_or_zip_code: Optional[str] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    state_or_province: Optional[str] = None

    street_name: Optional[str] = None

    street_suffix: Optional[str] = None


class CivicAddressListResponse(BaseModel):
    data: Optional[List[Data]] = None

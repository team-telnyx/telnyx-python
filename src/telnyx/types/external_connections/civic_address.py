# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .location import Location
from ..._models import BaseModel

__all__ = ["CivicAddress"]


class CivicAddress(BaseModel):
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

    locations: Optional[List[Location]] = None

    postal_or_zip_code: Optional[str] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    state_or_province: Optional[str] = None

    street_name: Optional[str] = None

    street_suffix: Optional[str] = None

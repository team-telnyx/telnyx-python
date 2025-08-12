# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DynamicEmergencyAddressListResponse", "Data", "Meta"]


class Data(BaseModel):
    administrative_area: str

    country_code: Literal["US", "CA", "PR"]

    house_number: str

    locality: str

    postal_code: str

    street_name: str

    id: Optional[str] = None

    created_at: Optional[str] = None
    """ISO 8601 formatted date of when the resource was created"""

    extended_address: Optional[str] = None

    house_suffix: Optional[str] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    sip_geolocation_id: Optional[str] = None
    """
    Unique location reference string to be used in SIP INVITE from / p-asserted
    headers.
    """

    status: Optional[Literal["pending", "activated", "rejected"]] = None
    """Status of dynamic emergency address"""

    street_post_directional: Optional[str] = None

    street_pre_directional: Optional[str] = None

    street_suffix: Optional[str] = None

    updated_at: Optional[str] = None
    """ISO 8601 formatted date of when the resource was last updated"""


class Meta(BaseModel):
    page_number: Optional[float] = None
    """Current Page based on pagination settings (included when defaults are used.)"""

    page_size: Optional[float] = None
    """
    Number of results to return per page based on pagination settings (included when
    defaults are used.)
    """

    total_pages: Optional[float] = None
    """Total number of pages based on pagination settings"""

    total_results: Optional[float] = None
    """Total number of results"""


class DynamicEmergencyAddressListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None

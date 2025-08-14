# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DynamicEmergencyEndpointListResponse", "Data", "Meta"]


class Data(BaseModel):
    callback_number: str

    caller_name: str

    dynamic_emergency_address_id: str
    """An id of a currently active dynamic emergency location."""

    id: Optional[str] = None

    created_at: Optional[str] = None
    """ISO 8601 formatted date of when the resource was created"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    sip_from_id: Optional[str] = None

    status: Optional[Literal["pending", "activated", "rejected"]] = None
    """Status of dynamic emergency address"""

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


class DynamicEmergencyEndpointListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None

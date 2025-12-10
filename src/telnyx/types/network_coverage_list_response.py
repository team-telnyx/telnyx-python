# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .available_service import AvailableService

__all__ = ["NetworkCoverageListResponse", "Location"]


class Location(BaseModel):
    code: Optional[str] = None
    """Location code."""

    name: Optional[str] = None
    """Human readable name of location."""

    pop: Optional[str] = None
    """Point of presence of location."""

    region: Optional[str] = None
    """Identifies the geographical region of location."""

    site: Optional[str] = None
    """Site of location."""


class NetworkCoverageListResponse(BaseModel):
    available_services: Optional[List[AvailableService]] = None
    """List of interface types supported in this region."""

    location: Optional[Location] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

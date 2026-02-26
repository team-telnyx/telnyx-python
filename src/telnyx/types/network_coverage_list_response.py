# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .available_service import AvailableService
from .shared.netapps_location import NetappsLocation

__all__ = ["NetworkCoverageListResponse"]


class NetworkCoverageListResponse(BaseModel):
    available_services: Optional[List[AvailableService]] = None
    """List of interface types supported in this region."""

    location: Optional[NetappsLocation] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

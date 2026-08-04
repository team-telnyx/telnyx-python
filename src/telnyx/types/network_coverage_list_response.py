# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .available_service import AvailableService
from .netapps_location_17904fcfbc import NetappsLocation17904fcfbc

__all__ = ["NetworkCoverageListResponse"]


class NetworkCoverageListResponse(BaseModel):
    available_services: Optional[List[AvailableService]] = None
    """List of interface types supported in this region."""

    location: Optional[NetappsLocation17904fcfbc] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

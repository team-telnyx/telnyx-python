# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.metadata import Metadata
from .dynamic_emergency_endpoint import DynamicEmergencyEndpoint

__all__ = ["DynamicEmergencyEndpointListResponse"]


class DynamicEmergencyEndpointListResponse(BaseModel):
    data: Optional[List[DynamicEmergencyEndpoint]] = None

    meta: Optional[Metadata] = None

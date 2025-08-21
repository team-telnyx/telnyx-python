# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .dynamic_emergency_endpoint import DynamicEmergencyEndpoint

__all__ = ["DynamicEmergencyEndpointDeleteResponse"]


class DynamicEmergencyEndpointDeleteResponse(BaseModel):
    data: Optional[DynamicEmergencyEndpoint] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .dynamic_emergency_endpoint import DynamicEmergencyEndpoint

__all__ = ["DynamicEmergencyEndpointCreateResponse"]


class DynamicEmergencyEndpointCreateResponse(BaseModel):
    data: Optional[DynamicEmergencyEndpoint] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .dynamic_emergency_address import DynamicEmergencyAddress

__all__ = ["DynamicEmergencyAddressDeleteResponse"]


class DynamicEmergencyAddressDeleteResponse(BaseModel):
    data: Optional[DynamicEmergencyAddress] = None

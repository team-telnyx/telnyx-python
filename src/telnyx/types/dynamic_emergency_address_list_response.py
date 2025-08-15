# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.metadata import Metadata
from .dynamic_emergency_address import DynamicEmergencyAddress

__all__ = ["DynamicEmergencyAddressListResponse"]


class DynamicEmergencyAddressListResponse(BaseModel):
    data: Optional[List[DynamicEmergencyAddress]] = None

    meta: Optional[Metadata] = None

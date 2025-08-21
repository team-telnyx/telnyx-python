# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .rcs_capabilities import RcsCapabilities

__all__ = ["RcListBulkCapabilitiesResponse"]


class RcListBulkCapabilitiesResponse(BaseModel):
    data: Optional[List[RcsCapabilities]] = None

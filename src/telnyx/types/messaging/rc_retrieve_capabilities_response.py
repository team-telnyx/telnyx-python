# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .rcs_capabilities import RcsCapabilities

__all__ = ["RcRetrieveCapabilitiesResponse"]


class RcRetrieveCapabilitiesResponse(BaseModel):
    data: Optional[RcsCapabilities] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .virtual_cross_connect_combined import VirtualCrossConnectCombined

__all__ = ["VirtualCrossConnectCreateResponse"]


class VirtualCrossConnectCreateResponse(BaseModel):
    data: Optional[VirtualCrossConnectCombined] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .portout_details import PortoutDetails

__all__ = ["PortoutUpdateStatusResponse"]


class PortoutUpdateStatusResponse(BaseModel):
    data: Optional[PortoutDetails] = None

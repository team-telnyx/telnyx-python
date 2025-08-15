# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .portout_details import PortoutDetails
from .shared.metadata import Metadata

__all__ = ["PortoutListResponse"]


class PortoutListResponse(BaseModel):
    data: Optional[List[PortoutDetails]] = None

    meta: Optional[Metadata] = None

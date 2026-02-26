# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .civic_address import CivicAddress

__all__ = ["CivicAddressListResponse"]


class CivicAddressListResponse(BaseModel):
    data: Optional[List[CivicAddress]] = None

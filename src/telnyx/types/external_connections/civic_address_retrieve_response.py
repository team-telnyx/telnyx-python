# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .civic_address import CivicAddress

__all__ = ["CivicAddressRetrieveResponse"]


class CivicAddressRetrieveResponse(BaseModel):
    data: Optional[CivicAddress] = None

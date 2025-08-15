# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .address import Address
from .._models import BaseModel

__all__ = ["AddressRetrieveResponse"]


class AddressRetrieveResponse(BaseModel):
    data: Optional[Address] = None

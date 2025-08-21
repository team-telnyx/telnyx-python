# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .address import Address
from .._models import BaseModel

__all__ = ["AddressDeleteResponse"]


class AddressDeleteResponse(BaseModel):
    data: Optional[Address] = None

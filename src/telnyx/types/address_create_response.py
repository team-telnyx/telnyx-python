# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .address import Address
from .._models import BaseModel

__all__ = ["AddressCreateResponse"]


class AddressCreateResponse(BaseModel):
    data: Optional[Address] = None

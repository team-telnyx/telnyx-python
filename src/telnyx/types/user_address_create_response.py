# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .user_addresses_user_address import UserAddressesUserAddress

__all__ = ["UserAddressCreateResponse"]


class UserAddressCreateResponse(BaseModel):
    data: Optional[UserAddressesUserAddress] = None

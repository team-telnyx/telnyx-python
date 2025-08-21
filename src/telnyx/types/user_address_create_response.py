# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .user_address import UserAddress

__all__ = ["UserAddressCreateResponse"]


class UserAddressCreateResponse(BaseModel):
    data: Optional[UserAddress] = None

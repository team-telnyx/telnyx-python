# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .user_bundle import UserBundle

__all__ = ["UserBundleCreateResponse"]


class UserBundleCreateResponse(BaseModel):
    data: List[UserBundle]

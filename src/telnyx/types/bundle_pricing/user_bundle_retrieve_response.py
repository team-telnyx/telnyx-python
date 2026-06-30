# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .user_bundle import UserBundle

__all__ = ["UserBundleRetrieveResponse"]


class UserBundleRetrieveResponse(BaseModel):
    data: UserBundle

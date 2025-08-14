# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .user_bundle_resource import UserBundleResource

__all__ = ["UserBundleListResourcesResponse"]


class UserBundleListResourcesResponse(BaseModel):
    data: List[UserBundleResource]

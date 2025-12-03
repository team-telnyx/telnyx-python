# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .user_bundle import UserBundle
from .pagination_response import PaginationResponse

__all__ = ["UserBundleListResponse"]


class UserBundleListResponse(BaseModel):
    data: List[UserBundle]

    meta: PaginationResponse

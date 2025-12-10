# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .oauth_grant import OAuthGrant
from .pagination_meta_oauth import PaginationMetaOAuth

__all__ = ["OAuthGrantListResponse"]


class OAuthGrantListResponse(BaseModel):
    data: Optional[List[OAuthGrant]] = None

    meta: Optional[PaginationMetaOAuth] = None

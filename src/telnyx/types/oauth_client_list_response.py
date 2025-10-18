# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .oauth_client import OAuthClient
from .pagination_meta_oauth import PaginationMetaOAuth

__all__ = ["OAuthClientListResponse"]


class OAuthClientListResponse(BaseModel):
    data: Optional[List[OAuthClient]] = None

    meta: Optional[PaginationMetaOAuth] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .authentication_provider import AuthenticationProvider

__all__ = ["AuthenticationProviderListResponse"]


class AuthenticationProviderListResponse(BaseModel):
    data: Optional[List[AuthenticationProvider]] = None

    meta: Optional[PaginationMeta] = None

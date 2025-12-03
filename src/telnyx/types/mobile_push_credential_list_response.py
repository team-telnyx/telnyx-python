# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .push_credential import PushCredential

__all__ = ["MobilePushCredentialListResponse"]


class MobilePushCredentialListResponse(BaseModel):
    data: Optional[List[PushCredential]] = None

    meta: Optional[PaginationMeta] = None

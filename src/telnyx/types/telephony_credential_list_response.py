# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .telephony_credential import TelephonyCredential

__all__ = ["TelephonyCredentialListResponse"]


class TelephonyCredentialListResponse(BaseModel):
    data: Optional[List[TelephonyCredential]] = None

    meta: Optional[PaginationMeta] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["MessagingURLDomainListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    record_type: Optional[str] = None

    url_domain: Optional[str] = None

    use_case: Optional[str] = None


class MessagingURLDomainListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

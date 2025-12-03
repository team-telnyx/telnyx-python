# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .doc_service_document import DocServiceDocument

__all__ = ["DocumentListResponse"]


class DocumentListResponse(BaseModel):
    data: Optional[List[DocServiceDocument]] = None

    meta: Optional[PaginationMeta] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .call_control_application import CallControlApplication

__all__ = ["CallControlApplicationListResponse"]


class CallControlApplicationListResponse(BaseModel):
    data: Optional[List[CallControlApplication]] = None

    meta: Optional[PaginationMeta] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .global_ip_assignment import GlobalIPAssignment

__all__ = ["GlobalIPAssignmentListResponse"]


class GlobalIPAssignmentListResponse(BaseModel):
    data: Optional[List[GlobalIPAssignment]] = None

    meta: Optional[PaginationMeta] = None

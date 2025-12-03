# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .job import Job
from ..._models import BaseModel
from ..pagination_meta import PaginationMeta

__all__ = ["JobListResponse"]


class JobListResponse(BaseModel):
    data: Optional[List[Job]] = None

    meta: Optional[PaginationMeta] = None

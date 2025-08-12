# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from .mdr_usage_report import MdrUsageReport

__all__ = ["MdrUsageReportListResponse"]


class MdrUsageReportListResponse(BaseModel):
    data: Optional[List[MdrUsageReport]] = None

    meta: Optional[PaginationMeta] = None

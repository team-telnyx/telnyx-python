# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .mdr_usage_report import MdrUsageReport
from .pagination_meta_reporting import PaginationMetaReporting

__all__ = ["MdrUsageReportListResponse"]


class MdrUsageReportListResponse(BaseModel):
    data: Optional[List[MdrUsageReport]] = None

    meta: Optional[PaginationMetaReporting] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .mdr_usage_report import MdrUsageReport

__all__ = ["MdrUsageReportListResponse", "Meta"]


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class MdrUsageReportListResponse(BaseModel):
    data: Optional[List[MdrUsageReport]] = None

    meta: Optional[Meta] = None

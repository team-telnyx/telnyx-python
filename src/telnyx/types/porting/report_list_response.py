# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .porting_report import PortingReport
from ..pagination_meta import PaginationMeta

__all__ = ["ReportListResponse"]


class ReportListResponse(BaseModel):
    data: Optional[List[PortingReport]] = None

    meta: Optional[PaginationMeta] = None

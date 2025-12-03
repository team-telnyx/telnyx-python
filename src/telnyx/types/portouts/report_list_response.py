# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .portout_report import PortoutReport
from ..pagination_meta import PaginationMeta

__all__ = ["ReportListResponse"]


class ReportListResponse(BaseModel):
    data: Optional[List[PortoutReport]] = None

    meta: Optional[PaginationMeta] = None

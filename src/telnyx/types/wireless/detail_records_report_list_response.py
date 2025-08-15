# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .wdr_report import WdrReport

__all__ = ["DetailRecordsReportListResponse"]


class DetailRecordsReportListResponse(BaseModel):
    data: Optional[List[WdrReport]] = None

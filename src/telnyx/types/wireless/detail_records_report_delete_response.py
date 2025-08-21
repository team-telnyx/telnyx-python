# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .wdr_report import WdrReport

__all__ = ["DetailRecordsReportDeleteResponse"]


class DetailRecordsReportDeleteResponse(BaseModel):
    data: Optional[WdrReport] = None

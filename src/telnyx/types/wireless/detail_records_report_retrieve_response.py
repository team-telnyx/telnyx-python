# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .wdr_report import WdrReport

__all__ = ["DetailRecordsReportRetrieveResponse"]


class DetailRecordsReportRetrieveResponse(BaseModel):
    data: Optional[WdrReport] = None

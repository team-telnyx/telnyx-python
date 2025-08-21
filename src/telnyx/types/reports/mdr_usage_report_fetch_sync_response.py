# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .mdr_usage_report import MdrUsageReport

__all__ = ["MdrUsageReportFetchSyncResponse"]


class MdrUsageReportFetchSyncResponse(BaseModel):
    data: Optional[MdrUsageReport] = None

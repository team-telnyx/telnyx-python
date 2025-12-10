# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from .telco_data_usage_report_response import TelcoDataUsageReportResponse

__all__ = ["NumberLookupCreateResponse"]


class NumberLookupCreateResponse(BaseModel):
    data: Optional[TelcoDataUsageReportResponse] = None
    """Telco data usage report response"""

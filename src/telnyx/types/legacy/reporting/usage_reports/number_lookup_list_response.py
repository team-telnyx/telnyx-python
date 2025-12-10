# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .standard_pagination_meta import StandardPaginationMeta
from .telco_data_usage_report_response import TelcoDataUsageReportResponse

__all__ = ["NumberLookupListResponse"]


class NumberLookupListResponse(BaseModel):
    data: Optional[List[TelcoDataUsageReportResponse]] = None

    meta: Optional[StandardPaginationMeta] = None

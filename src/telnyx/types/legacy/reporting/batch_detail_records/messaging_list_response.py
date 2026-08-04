# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ....._models import BaseModel
from .mdr_detail_report_response import MdrDetailReportResponse
from .batch_csv_pagination_meta_705dfa7312 import BatchCsvPaginationMeta705dfa7312

__all__ = ["MessagingListResponse"]


class MessagingListResponse(BaseModel):
    data: Optional[List[MdrDetailReportResponse]] = None

    meta: Optional[BatchCsvPaginationMeta705dfa7312] = None

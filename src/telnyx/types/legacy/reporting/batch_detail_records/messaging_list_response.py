# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .batch_csv_pagination_meta import BatchCsvPaginationMeta
from .mdr_detail_report_response import MdrDetailReportResponse

__all__ = ["MessagingListResponse"]


class MessagingListResponse(BaseModel):
    data: Optional[List[MdrDetailReportResponse]] = None

    meta: Optional[BatchCsvPaginationMeta] = None

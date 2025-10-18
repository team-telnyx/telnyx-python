# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .standard_pagination_meta import StandardPaginationMeta
from .mdr_usage_report_response_legacy import MdrUsageReportResponseLegacy

__all__ = ["MessagingListResponse"]


class MessagingListResponse(BaseModel):
    data: Optional[List[MdrUsageReportResponseLegacy]] = None

    meta: Optional[StandardPaginationMeta] = None

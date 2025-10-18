# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .standard_pagination_meta import StandardPaginationMeta
from .cdr_usage_report_response_legacy import CdrUsageReportResponseLegacy

__all__ = ["VoiceListResponse"]


class VoiceListResponse(BaseModel):
    data: Optional[List[CdrUsageReportResponseLegacy]] = None

    meta: Optional[StandardPaginationMeta] = None

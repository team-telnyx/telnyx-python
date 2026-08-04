# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ....._models import BaseModel
from .cdr_detailed_req_response import CdrDetailedReqResponse
from .batch_csv_pagination_meta_705dfa7312 import BatchCsvPaginationMeta705dfa7312

__all__ = ["VoiceListResponse"]


class VoiceListResponse(BaseModel):
    data: Optional[List[CdrDetailedReqResponse]] = None

    meta: Optional[BatchCsvPaginationMeta705dfa7312] = None

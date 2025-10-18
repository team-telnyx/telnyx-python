# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .batch_csv_pagination_meta import BatchCsvPaginationMeta
from .cdr_detailed_req_response import CdrDetailedReqResponse

__all__ = ["VoiceListResponse"]


class VoiceListResponse(BaseModel):
    data: Optional[List[CdrDetailedReqResponse]] = None

    meta: Optional[BatchCsvPaginationMeta] = None

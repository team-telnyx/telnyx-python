# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .cdr_detailed_req_response import CdrDetailedReqResponse

__all__ = ["VoiceListResponse", "Meta"]


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class VoiceListResponse(BaseModel):
    data: Optional[List[CdrDetailedReqResponse]] = None

    meta: Optional[Meta] = None

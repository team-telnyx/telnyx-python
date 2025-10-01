# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from .mdr_detail_report_response import MdrDetailReportResponse

__all__ = ["MessagingListResponse", "Meta"]


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class MessagingListResponse(BaseModel):
    data: Optional[List[MdrDetailReportResponse]] = None

    meta: Optional[Meta] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from .mdr_detail_report_response import MdrDetailReportResponse

__all__ = ["MessagingDeleteResponse"]


class MessagingDeleteResponse(BaseModel):
    data: Optional[MdrDetailReportResponse] = None

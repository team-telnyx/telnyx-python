# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ....._models import BaseModel
from .stt_detail_report_response import SttDetailReportResponse

__all__ = ["SpeechToTextDeleteResponse"]


class SpeechToTextDeleteResponse(BaseModel):
    data: Optional[SttDetailReportResponse] = None

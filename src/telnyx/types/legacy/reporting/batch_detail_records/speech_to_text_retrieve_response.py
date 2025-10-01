# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from .stt_detail_report_response import SttDetailReportResponse

__all__ = ["SpeechToTextRetrieveResponse"]


class SpeechToTextRetrieveResponse(BaseModel):
    data: Optional[SttDetailReportResponse] = None

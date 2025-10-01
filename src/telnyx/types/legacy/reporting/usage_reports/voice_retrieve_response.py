# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from .cdr_usage_report_response_legacy import CdrUsageReportResponseLegacy

__all__ = ["VoiceRetrieveResponse"]


class VoiceRetrieveResponse(BaseModel):
    data: Optional[CdrUsageReportResponseLegacy] = None
    """Legacy V2 CDR usage report response"""

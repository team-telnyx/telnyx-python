# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel
from .cdr_detailed_req_response import CdrDetailedReqResponse

__all__ = ["VoiceCreateResponse"]


class VoiceCreateResponse(BaseModel):
    data: Optional[CdrDetailedReqResponse] = None
    """Response object for CDR detailed report"""

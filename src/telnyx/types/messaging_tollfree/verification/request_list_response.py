# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .verification_request_status import VerificationRequestStatus

__all__ = ["RequestListResponse"]


class RequestListResponse(BaseModel):
    records: Optional[List[VerificationRequestStatus]] = None
    """The records yielded by this request"""

    total_records: Optional[int] = None
    """The total amount of records for these query parameters"""

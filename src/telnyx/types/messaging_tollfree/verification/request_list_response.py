# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .verification_request_status import VerificationRequestStatus

__all__ = ["RequestListResponse"]


class RequestListResponse(BaseModel):
    """A paginated response"""

    records: List[VerificationRequestStatus]
    """The records yielded by this request"""

    total_records: int
    """The total amount of records for these query parameters"""

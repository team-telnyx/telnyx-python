# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .tf_verification_status import TfVerificationStatus

__all__ = ["RequestRetrieveStatusHistoryResponse", "Record"]


class Record(BaseModel):
    """A single entry in the verification request status history"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The timestamp at which this status change occurred"""

    verification_status: TfVerificationStatus = FieldInfo(alias="verificationStatus")
    """Tollfree verification status"""

    reason: Optional[str] = None
    """An explanation of why this request has its current status."""


class RequestRetrieveStatusHistoryResponse(BaseModel):
    """A paginated response"""

    records: List[Record]
    """The records yielded by this request"""

    total_records: int
    """The total amount of records for these query parameters"""

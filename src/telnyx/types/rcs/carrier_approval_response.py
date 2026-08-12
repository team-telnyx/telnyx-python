# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CarrierApprovalResponse"]


class CarrierApprovalResponse(BaseModel):
    approval_id: str

    approved_at: Optional[datetime] = None

    carrier: Optional[str] = None

    rejected_reason: Optional[str] = None

    scope_type: Literal["carrier", "hub", "bot"]

    status: Literal["PENDING", "SUBMITTED", "APPROVED", "REJECTED"]

    submitted_at: Optional[datetime] = None

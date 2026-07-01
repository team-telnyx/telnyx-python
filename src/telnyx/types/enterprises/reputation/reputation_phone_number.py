# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from ...shared.reputation_data import ReputationData

__all__ = ["ReputationPhoneNumber"]


class ReputationPhoneNumber(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    enterprise_id: Optional[str] = None

    phone_number: Optional[str] = None
    """E.164 with leading `+`."""

    reputation_data: Optional[ReputationData] = None
    """`null` until the first refresh has been collected for this number."""

    updated_at: Optional[datetime] = None

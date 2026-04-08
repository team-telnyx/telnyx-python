# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .reputation_data import ReputationData

__all__ = ["ReputationPhoneNumberWithReputationData"]


class ReputationPhoneNumberWithReputationData(BaseModel):
    id: Optional[str] = None
    """Unique identifier"""

    created_at: Optional[datetime] = None
    """When the number was associated"""

    enterprise_id: Optional[str] = None
    """ID of the associated enterprise"""

    phone_number: Optional[str] = None
    """Phone number in E.164 format"""

    reputation_data: Optional[ReputationData] = None
    """Reputation metrics"""

    updated_at: Optional[datetime] = None
    """When the record was last updated"""

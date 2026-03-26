# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EnterpriseReputationPublic"]


class EnterpriseReputationPublic(BaseModel):
    check_frequency: Optional[Literal["business_daily", "daily", "weekly", "biweekly", "monthly", "never"]] = None
    """Frequency for refreshing reputation data"""

    created_at: Optional[datetime] = None
    """When the reputation settings were created"""

    enterprise_id: Optional[str] = None
    """ID of the associated enterprise"""

    loa_document_id: Optional[str] = None
    """ID of the signed LOA document"""

    rejection_reasons: Optional[List[str]] = None
    """Reasons for rejection (present when status is rejected)"""

    status: Optional[Literal["pending", "approved", "rejected", "deleted"]] = None
    """Current enrollment status"""

    updated_at: Optional[datetime] = None
    """When the reputation settings were last updated"""

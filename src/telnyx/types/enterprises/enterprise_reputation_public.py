# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .reputation_check_frequency import ReputationCheckFrequency

__all__ = ["EnterpriseReputationPublic"]


class EnterpriseReputationPublic(BaseModel):
    check_frequency: Optional[ReputationCheckFrequency] = None
    """
    How often Telnyx refreshes the stored reputation data for this enterprise's
    registered numbers.
    """

    created_at: Optional[datetime] = None

    enterprise_id: Optional[str] = None

    loa_document_id: Optional[str] = None
    """Id of the signed LOA document."""

    loa_status: Optional[Literal["pending", "approved", "rejected"]] = None
    """Customer-facing Letter-of-Authorization verification state.

    `approved` is required (alongside reputation status) before phone numbers can be
    added.
    """

    rejection_reasons: Optional[List[str]] = None
    """Populated when `status` is `rejected`."""

    status: Optional[Literal["pending", "approved", "deleted", "rejected"]] = None
    """Lifecycle status of the enterprise's Phone Number Reputation activation."""

    updated_at: Optional[datetime] = None

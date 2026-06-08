# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["RemediationListResponse"]


class RemediationListResponse(BaseModel):
    """Slim list-endpoint shape.

    Omits per-number results and webhook URLs to keep responses small.
    """

    id: str

    call_purpose: str

    created_at: datetime

    phone_numbers_count: int

    status: Literal["pending", "in_progress", "completed", "failed", "cancelled"]
    """Customer-facing status of a remediation request."""

    updated_at: datetime

    tier1_completed_at: Optional[datetime] = None

    tier2_completed_at: Optional[datetime] = None

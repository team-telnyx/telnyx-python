# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .remediation_status import RemediationStatus
from .remediation_per_number_results import RemediationPerNumberResults

__all__ = ["RemediationRequest"]


class RemediationRequest(BaseModel):
    """Full detail of a remediation request, returned on submit and GET by id."""

    id: str

    call_purpose: str

    created_at: datetime

    phone_numbers_count: int
    """Total phone numbers in this batch, including any later cancelled.

    May exceed the sum of the per-category result buckets, which omit cancelled
    numbers.
    """

    phone_numbers_ineligible: int
    """Numbers rejected before submission (e.g. cooldown)."""

    phone_numbers_submitted: int
    """Numbers accepted for remediation, i.e.

    not rejected as ineligible. Counts numbers still queued (pending) as well as
    processed ones.
    """

    status: RemediationStatus
    """Customer-facing status of a remediation request."""

    updated_at: datetime

    contact_email: Optional[str] = None

    results: Optional[RemediationPerNumberResults] = None
    """Per-category buckets.

    Populated once results are available. Null while the request is still pending.
    """

    tier1_completed_at: Optional[datetime] = None

    tier2_completed_at: Optional[datetime] = None

    webhook_url: Optional[str] = None

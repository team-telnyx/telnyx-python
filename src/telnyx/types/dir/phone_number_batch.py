# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..document import Document
from .dir_phone_number import DirPhoneNumber
from .dir_phone_number_status import DirPhoneNumberStatus

__all__ = ["PhoneNumberBatch"]


class PhoneNumberBatch(BaseModel):
    """A phone-number batch groups all numbers added in a single bulk-add request.

    Telnyx vets the batch as a unit. The response embeds the full `phone_numbers` array so you can read per-number status without a separate call, plus a batch-level `status` summarising the unit's progress.
    """

    batch_id: Optional[str] = None

    dir_display_name: Optional[str] = None
    """The DIR's display name at the time the batch was read."""

    dir_id: Optional[str] = None

    documents: Optional[List[Document]] = None
    """Documents attached to this batch (e.g.

    a Letter of Authorization). Empty when none were supplied at add time.
    """

    enterprise_id: Optional[str] = None

    phone_numbers: Optional[List[DirPhoneNumber]] = None
    """All phone numbers in this batch, with per-number status."""

    status: Optional[DirPhoneNumberStatus] = None
    """Aggregate batch status.

    Mirrors the values used on individual phone numbers (`submitted`, `in_review`,
    `verified`, `unsuccessful`, `permanently_rejected`, etc.).
    """

    submitted_at: Optional[datetime] = None
    """When the batch was created (and implicitly submitted for vetting)."""

    total_count: Optional[int] = None
    """Number of phone numbers in this batch (length of `phone_numbers`)."""

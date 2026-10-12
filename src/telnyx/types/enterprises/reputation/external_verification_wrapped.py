# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from .external_verification_status import ExternalVerificationStatus

__all__ = ["ExternalVerificationWrapped", "Data"]


class Data(BaseModel):
    document_ids: Optional[List[str]] = None
    """The ownership-proof documents on file."""

    enterprise_id: Optional[str] = None

    phone_numbers: Optional[List[str]] = None
    """The phone numbers you listed with the documents."""

    rejection_reason: Optional[str] = None
    """Why the proof was rejected. Set only when `status` is `rejected`."""

    reviewed_at: Optional[datetime] = None

    status: Optional[ExternalVerificationStatus] = None
    """
    Review state of the ownership proof that allows adding phone numbers hosted with
    another provider.
    """

    submitted_at: Optional[datetime] = None


class ExternalVerificationWrapped(BaseModel):
    data: Data

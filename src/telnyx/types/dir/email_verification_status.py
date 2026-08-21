# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EmailVerificationStatus"]


class EmailVerificationStatus(BaseModel):
    """Verification state for a DIR's authorizer email."""

    email_verified: bool
    """Whether the DIR's authorizer email has been confirmed."""

    record_type: Literal["email_verification"]
    """Always `email_verification`."""

    status: Literal["sent", "verified", "unverified"]
    """
    `sent` after a code is emailed; `verified` after a successful confirm;
    `unverified` when no verification is in progress.
    """

    expires_at: Optional[datetime] = None
    """When the outstanding code stops being accepted.

    Null when no verification is in progress.
    """

    sends_remaining_today: Optional[int] = None
    """How many more codes may be requested for this DIR today.

    Null when the daily cap does not apply.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EnterpriseEmailVerificationStatusWrapped", "Data"]


class Data(BaseModel):
    """Verification state for an enterprise account's contact email."""

    email_verified: bool
    """Whether the enterprise account's contact email has been confirmed."""

    record_type: Literal["email_verification"]
    """Always `email_verification`."""

    status: Literal["sent", "verified"]
    """`sent` after a code is emailed; `verified` after a successful confirm."""

    expires_at: Optional[datetime] = None
    """When the code just sent stops being accepted.

    Present on a send response; null on a confirm response.
    """

    sends_remaining_today: Optional[int] = None
    """How many more codes may be requested for this enterprise account today.

    Present on a send response; null on a confirm response.
    """


class EnterpriseEmailVerificationStatusWrapped(BaseModel):
    data: Data
    """Verification state for an enterprise account's contact email."""

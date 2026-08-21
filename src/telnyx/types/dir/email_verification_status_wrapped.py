# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .email_verification_status import EmailVerificationStatus

__all__ = ["EmailVerificationStatusWrapped"]


class EmailVerificationStatusWrapped(BaseModel):
    data: EmailVerificationStatus
    """Verification state for a DIR's authorizer email."""

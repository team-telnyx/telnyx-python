# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .enterprise_email_verification_status import EnterpriseEmailVerificationStatus

__all__ = ["EnterpriseEmailVerificationStatusWrapped"]


class EnterpriseEmailVerificationStatusWrapped(BaseModel):
    data: EnterpriseEmailVerificationStatus
    """Verification state for an enterprise account's contact email."""

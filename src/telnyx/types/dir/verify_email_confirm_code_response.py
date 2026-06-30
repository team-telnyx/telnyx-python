# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VerifyEmailConfirmCodeResponse", "Data"]


class Data(BaseModel):
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


class VerifyEmailConfirmCodeResponse(BaseModel):
    data: Data
    """Verification state for a DIR's authorizer email."""

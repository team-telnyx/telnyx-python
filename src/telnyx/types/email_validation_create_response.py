# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .email_validation_checks import EmailValidationChecks

__all__ = ["EmailValidationCreateResponse", "Data"]


class Data(BaseModel):
    checks: EmailValidationChecks

    email: str

    record_type: Literal["email_validation"]

    risk_score: float

    valid: bool

    did_you_mean: Optional[str] = None
    """Suggested correction for typo. Omitted when nil."""


class EmailValidationCreateResponse(BaseModel):
    data: Data

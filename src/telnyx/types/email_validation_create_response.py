# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .email_validation_check import EmailValidationCheck

__all__ = ["EmailValidationCreateResponse", "Data", "DataChecks", "DataChecksTypo"]


class DataChecksTypo(EmailValidationCheck):
    suggestion: Optional[str] = None
    """Suggested correction for common typos. Omitted when nil."""


class DataChecks(BaseModel):
    disposable: EmailValidationCheck

    mx: EmailValidationCheck

    role_based: EmailValidationCheck

    syntax: EmailValidationCheck

    typo: DataChecksTypo


class Data(BaseModel):
    checks: DataChecks

    email: str

    record_type: Literal["email_validation"]

    risk_score: float

    valid: bool

    did_you_mean: Optional[str] = None
    """Suggested correction for typo. Omitted when nil."""


class EmailValidationCreateResponse(BaseModel):
    data: Data

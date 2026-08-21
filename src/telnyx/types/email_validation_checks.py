# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .email_validation_check import EmailValidationCheck

__all__ = ["EmailValidationChecks", "Typo"]


class Typo(EmailValidationCheck):
    suggestion: Optional[str] = None
    """Suggested correction for common typos. Omitted when nil."""


class EmailValidationChecks(BaseModel):
    disposable: EmailValidationCheck

    mx: EmailValidationCheck

    role_based: EmailValidationCheck

    syntax: EmailValidationCheck

    typo: Typo

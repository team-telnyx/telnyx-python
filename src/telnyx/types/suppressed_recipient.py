# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["SuppressedRecipient"]


class SuppressedRecipient(BaseModel):
    override_allowed: bool
    """Whether an authorized send may override this suppression."""

    reason: str
    """Suppression reason returned by the recipient suppression service."""

    scope: str
    """Scope at which the suppression applies."""

    to: str
    """Suppressed recipient email address."""

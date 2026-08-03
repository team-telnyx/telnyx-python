# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .email_message import EmailMessage

__all__ = ["EmailMessageResponse", "Suppressed"]


class Suppressed(BaseModel):
    override_allowed: bool
    """Whether an authorized send may override this suppression."""

    reason: str
    """Suppression reason returned by the recipient suppression service."""

    scope: str
    """Scope at which the suppression applies."""

    to: str
    """Suppressed recipient email address."""


class EmailMessageResponse(BaseModel):
    data: EmailMessage

    suppressed: Optional[List[Suppressed]] = None
    """
    Recipients removed by suppression checks when at least one recipient remains and
    the message is accepted.
    """

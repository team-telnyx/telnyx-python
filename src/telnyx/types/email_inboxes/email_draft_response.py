# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .email_draft import EmailDraft

__all__ = ["EmailDraftResponse"]


class EmailDraftResponse(BaseModel):
    data: EmailDraft
    """An unsent, mutable draft message belonging to an inbox."""

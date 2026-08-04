# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .email_inbox import EmailInbox

__all__ = ["EmailInboxListResponse", "Meta"]


class Meta(BaseModel):
    page_size: int

    page_cursor: Optional[str] = None
    """Cursor for the next inbox page, when more results are available."""


class EmailInboxListResponse(BaseModel):
    data: List[EmailInbox]

    meta: Meta

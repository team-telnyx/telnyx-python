# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .email_recipient import EmailRecipient

__all__ = ["RecipientListResponse", "Meta"]


class Meta(BaseModel):
    page_size: int

    page_cursor: Optional[str] = None
    """Cursor for the next page. Absent when there are no more results."""


class RecipientListResponse(BaseModel):
    data: List[EmailRecipient]

    meta: Meta

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel
from .email_draft import EmailDraft
from .email_pagination_meta import EmailPaginationMeta

__all__ = ["DraftListResponse"]


class DraftListResponse(BaseModel):
    data: List[EmailDraft]

    meta: EmailPaginationMeta

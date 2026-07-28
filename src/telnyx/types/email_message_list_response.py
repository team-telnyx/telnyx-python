# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel
from .email_inboxes.email_message import EmailMessage
from .email_inboxes.email_pagination_meta import EmailPaginationMeta

__all__ = ["EmailMessageListResponse"]


class EmailMessageListResponse(BaseModel):
    data: List[EmailMessage]

    meta: EmailPaginationMeta

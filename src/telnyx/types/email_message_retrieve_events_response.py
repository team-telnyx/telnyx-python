# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel
from .message_event import MessageEvent
from .email_inboxes.email_pagination_meta import EmailPaginationMeta

__all__ = ["EmailMessageRetrieveEventsResponse"]


class EmailMessageRetrieveEventsResponse(BaseModel):
    data: List[MessageEvent]

    meta: EmailPaginationMeta

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel
from ..inbound_message import InboundMessage
from .email_pagination_meta import EmailPaginationMeta

__all__ = ["MessageListResponse"]


class MessageListResponse(BaseModel):
    data: List[InboundMessage]

    meta: EmailPaginationMeta

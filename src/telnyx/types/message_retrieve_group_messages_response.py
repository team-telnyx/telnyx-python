# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .messaging_outbound_message_payload import MessagingOutboundMessagePayload

__all__ = ["MessageRetrieveGroupMessagesResponse"]


class MessageRetrieveGroupMessagesResponse(BaseModel):
    data: Optional[List[MessagingOutboundMessagePayload]] = None

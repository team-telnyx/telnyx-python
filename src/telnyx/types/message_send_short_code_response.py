# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .messaging_outbound_message_payload import MessagingOutboundMessagePayload

__all__ = ["MessageSendShortCodeResponse"]


class MessageSendShortCodeResponse(BaseModel):
    data: Optional[MessagingOutboundMessagePayload] = None

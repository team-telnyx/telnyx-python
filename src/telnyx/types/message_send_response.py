# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .outbound_message_payload import OutboundMessagePayload

__all__ = ["MessageSendResponse"]


class MessageSendResponse(BaseModel):
    data: Optional[OutboundMessagePayload] = None

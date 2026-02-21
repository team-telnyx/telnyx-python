# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .outbound_message_payload import OutboundMessagePayload

__all__ = ["MessageRetrieveGroupMessagesResponse"]


class MessageRetrieveGroupMessagesResponse(BaseModel):
    data: Optional[List[OutboundMessagePayload]] = None

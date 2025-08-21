# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .outbound_message_payload import OutboundMessagePayload

__all__ = ["MessageScheduleResponse"]


class MessageScheduleResponse(BaseModel):
    data: Optional[OutboundMessagePayload] = None

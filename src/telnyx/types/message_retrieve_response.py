# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .messaging_inbound_message_payload import MessagingInboundMessagePayload
from .messaging_outbound_message_payload import MessagingOutboundMessagePayload

__all__ = ["MessageRetrieveResponse", "Data"]

Data: TypeAlias = Annotated[
    Union[MessagingOutboundMessagePayload, MessagingInboundMessagePayload], PropertyInfo(discriminator="direction")
]


class MessageRetrieveResponse(BaseModel):
    data: Optional[Data] = None

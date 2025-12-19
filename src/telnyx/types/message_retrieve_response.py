# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .outbound_message_payload import OutboundMessagePayload
from .shared.inbound_message_payload import InboundMessagePayload

__all__ = ["MessageRetrieveResponse", "Data"]

Data: TypeAlias = Annotated[
    Union[OutboundMessagePayload, InboundMessagePayload], PropertyInfo(discriminator="direction")
]


class MessageRetrieveResponse(BaseModel):
    data: Optional[Data] = None

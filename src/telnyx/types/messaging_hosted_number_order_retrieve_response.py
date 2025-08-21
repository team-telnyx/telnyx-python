# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.messaging_hosted_number_order import MessagingHostedNumberOrder

__all__ = ["MessagingHostedNumberOrderRetrieveResponse"]


class MessagingHostedNumberOrderRetrieveResponse(BaseModel):
    data: Optional[MessagingHostedNumberOrder] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.messaging_hosted_number_order import MessagingHostedNumberOrder

__all__ = ["MessagingHostedNumberOrderListResponse", "Meta"]


class Meta(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int


class MessagingHostedNumberOrderListResponse(BaseModel):
    data: Optional[List[MessagingHostedNumberOrder]] = None

    meta: Optional[Meta] = None

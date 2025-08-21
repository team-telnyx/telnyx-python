# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .shared.messaging_hosted_number_order import MessagingHostedNumberOrder

__all__ = ["MessagingHostedNumberOrderListResponse"]


class MessagingHostedNumberOrderListResponse(BaseModel):
    data: Optional[List[MessagingHostedNumberOrder]] = None

    meta: Optional[PaginationMeta] = None

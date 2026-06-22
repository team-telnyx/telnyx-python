# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .porting_orders_comment import PortingOrdersComment

__all__ = ["CommentCreateResponse"]


class CommentCreateResponse(BaseModel):
    data: Optional[PortingOrdersComment] = None

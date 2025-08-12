# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta

__all__ = ["CommentListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    body: Optional[str] = None
    """Body of comment"""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    porting_order_id: Optional[str] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    user_type: Optional[Literal["admin", "user", "system"]] = None
    """Indicates whether this comment was created by a Telnyx Admin, user, or system"""


class CommentListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None

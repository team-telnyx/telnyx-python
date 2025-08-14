# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CommentCreateResponse", "Data"]


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


class CommentCreateResponse(BaseModel):
    data: Optional[Data] = None

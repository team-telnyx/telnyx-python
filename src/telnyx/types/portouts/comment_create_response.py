# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CommentCreateResponse", "Data"]


class Data(BaseModel):
    id: str

    body: str
    """Comment body"""

    created_at: str
    """Comment creation timestamp in ISO 8601 format"""

    user_id: str
    """Identifies the user who created the comment.

    Will be null if created by Telnyx Admin
    """

    portout_id: Optional[str] = None
    """Identifies the associated port request"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class CommentCreateResponse(BaseModel):
    data: Optional[Data] = None

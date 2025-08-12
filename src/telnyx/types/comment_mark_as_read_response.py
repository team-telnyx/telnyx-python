# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CommentMarkAsReadResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    body: Optional[str] = None

    comment_record_id: Optional[str] = None

    comment_record_type: Optional[Literal["sub_number_order", "requirement_group"]] = None

    commenter: Optional[str] = None

    commenter_type: Optional[Literal["admin", "user"]] = None

    created_at: Optional[datetime] = None
    """An ISO 8901 datetime string denoting when the comment was created."""

    read_at: Optional[datetime] = None
    """An ISO 8901 datetime string for when the comment was read."""

    updated_at: Optional[datetime] = None
    """An ISO 8901 datetime string for when the comment was updated."""


class CommentMarkAsReadResponse(BaseModel):
    data: Optional[Data] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .comment import Comment
from .._models import BaseModel

__all__ = ["CommentMarkAsReadResponse", "Data"]


class Data(Comment):
    pass


class CommentMarkAsReadResponse(BaseModel):
    data: Optional[Data] = None

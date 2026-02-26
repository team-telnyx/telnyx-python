# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .comment import Comment
from .._models import BaseModel

__all__ = ["CommentRetrieveResponse", "Data"]


class Data(Comment):
    pass


class CommentRetrieveResponse(BaseModel):
    data: Optional[Data] = None

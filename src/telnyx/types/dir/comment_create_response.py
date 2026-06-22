# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .dir_comment import DirComment

__all__ = ["CommentCreateResponse"]


class CommentCreateResponse(BaseModel):
    data: DirComment

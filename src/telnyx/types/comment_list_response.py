# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .comment import Comment
from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["CommentListResponse"]


class CommentListResponse(BaseModel):
    data: Optional[List[Comment]] = None

    meta: Optional[PaginationMeta] = None

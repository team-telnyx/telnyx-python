# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .portout_comment import PortoutComment
from ..shared.metadata import Metadata

__all__ = ["CommentListResponse"]


class CommentListResponse(BaseModel):
    data: Optional[List[PortoutComment]] = None

    meta: Optional[Metadata] = None

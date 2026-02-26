# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .portout_comment import PortoutComment

__all__ = ["CommentCreateResponse"]


class CommentCreateResponse(BaseModel):
    data: Optional[PortoutComment] = None

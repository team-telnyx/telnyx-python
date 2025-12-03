# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .messaging_profile import MessagingProfile

__all__ = ["MessagingProfileListResponse"]


class MessagingProfileListResponse(BaseModel):
    data: Optional[List[MessagingProfile]] = None

    meta: Optional[PaginationMeta] = None

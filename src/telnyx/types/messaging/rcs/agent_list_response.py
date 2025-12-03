# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...rcs_agent import RcsAgent
from ...pagination_meta import PaginationMeta

__all__ = ["AgentListResponse"]


class AgentListResponse(BaseModel):
    data: Optional[List[RcsAgent]] = None

    meta: Optional[PaginationMeta] = None

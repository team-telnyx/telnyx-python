# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...rcs_agent import RcsAgent

__all__ = ["AgentListResponse", "Meta"]


class Meta(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int


class AgentListResponse(BaseModel):
    data: Optional[List[RcsAgent]] = None

    meta: Optional[Meta] = None

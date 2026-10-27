# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .test_agent import TestAgent
from ......_models import BaseModel

__all__ = ["AiagentListResponse"]


class AiagentListResponse(BaseModel):
    count: int

    next: Optional[str] = None
    """Link to the next page of results, or null."""

    previous: Optional[str] = None
    """Link to the previous page of results, or null."""

    results: List[TestAgent]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .research_citation import ResearchCitation

__all__ = ["ResearchCreateResponse", "Data", "DataResearchResponseSync", "DataResearchResponseAsync"]


class DataResearchResponseSync(BaseModel):
    """Synchronous research response (when `background` is false or unset)."""

    answer: str
    """The synthesized research answer."""

    citations: Optional[List[ResearchCitation]] = None
    """Sources cited in the answer."""


class DataResearchResponseAsync(BaseModel):
    """Asynchronous research response (when `background` is true)."""

    status: Literal["pending", "running", "completed", "failed"]
    """Current status of the research task."""

    task_id: str
    """Unique identifier for the research task. Use this to poll the status."""


Data: TypeAlias = Union[DataResearchResponseSync, DataResearchResponseAsync]


class ResearchCreateResponse(BaseModel):
    data: Optional[Data] = None
    """Synchronous research response (when `background` is false or unset)."""

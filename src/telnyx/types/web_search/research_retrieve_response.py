# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .research_citation import ResearchCitation

__all__ = ["ResearchRetrieveResponse", "Data"]


class Data(BaseModel):
    status: Literal["pending", "running", "completed", "failed"]
    """Current status of the research task."""

    task_id: str
    """The research task identifier."""

    answer: Optional[str] = None
    """The synthesized research answer (present when status is `completed`)."""

    citations: Optional[List[ResearchCitation]] = None
    """Sources cited in the answer (present when status is `completed`)."""

    error: Optional[str] = None
    """Always present in poll responses; `null` unless the task failed."""


class ResearchRetrieveResponse(BaseModel):
    data: Optional[Data] = None

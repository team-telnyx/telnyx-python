# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["PlanRetrieveResponse", "Data"]


class Data(BaseModel):
    description: str

    run_id: str

    sequence: int

    status: Literal["pending", "in_progress", "completed", "skipped", "failed"]

    step_id: str

    completed_at: Optional[datetime] = None

    metadata: Optional[Dict[str, object]] = None

    parent_step_id: Optional[str] = None

    started_at: Optional[datetime] = None


class PlanRetrieveResponse(BaseModel):
    data: List[Data]

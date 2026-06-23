# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ....._models import BaseModel
from .step_status import StepStatus

__all__ = ["PlanStepData"]


class PlanStepData(BaseModel):
    description: str

    run_id: str

    sequence: int

    status: StepStatus

    step_id: str

    completed_at: Optional[datetime] = None

    metadata: Optional[Dict[str, object]] = None

    parent_step_id: Optional[str] = None

    started_at: Optional[datetime] = None

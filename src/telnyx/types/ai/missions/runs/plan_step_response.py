# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._models import BaseModel
from .plan_step_data import PlanStepData

__all__ = ["PlanStepResponse"]


class PlanStepResponse(BaseModel):
    data: PlanStepData

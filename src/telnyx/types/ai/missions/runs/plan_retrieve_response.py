# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .plan_step_data import PlanStepData

__all__ = ["PlanRetrieveResponse"]


class PlanRetrieveResponse(BaseModel):
    data: List[PlanStepData]

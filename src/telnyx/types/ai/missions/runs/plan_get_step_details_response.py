# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel
from .plan_step_data import PlanStepData

__all__ = ["PlanGetStepDetailsResponse"]


class PlanGetStepDetailsResponse(BaseModel):
    data: PlanStepData

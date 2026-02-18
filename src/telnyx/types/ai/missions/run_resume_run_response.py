# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .mission_run_data import MissionRunData

__all__ = ["RunResumeRunResponse"]


class RunResumeRunResponse(BaseModel):
    data: MissionRunData

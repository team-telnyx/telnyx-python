# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._models import BaseModel
from .mission_run_data import MissionRunData

__all__ = ["MissionRunResponse"]


class MissionRunResponse(BaseModel):
    data: MissionRunData

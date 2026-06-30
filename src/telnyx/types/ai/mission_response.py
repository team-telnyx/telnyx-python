# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .mission_data import MissionData

__all__ = ["MissionResponse"]


class MissionResponse(BaseModel):
    data: MissionData

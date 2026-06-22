# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel
from .execution_mode import ExecutionMode

__all__ = ["MissionData"]


class MissionData(BaseModel):
    created_at: datetime

    execution_mode: ExecutionMode

    mission_id: str

    name: str

    updated_at: datetime

    description: Optional[str] = None

    instructions: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    model: Optional[str] = None

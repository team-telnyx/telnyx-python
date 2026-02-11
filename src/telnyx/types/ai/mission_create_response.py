# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MissionCreateResponse", "Data"]


class Data(BaseModel):
    created_at: datetime

    execution_mode: Literal["external", "managed"]

    mission_id: str

    name: str

    updated_at: datetime

    description: Optional[str] = None

    instructions: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    model: Optional[str] = None


class MissionCreateResponse(BaseModel):
    data: Data

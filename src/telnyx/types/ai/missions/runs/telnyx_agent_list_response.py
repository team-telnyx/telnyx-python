# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ....._models import BaseModel

__all__ = ["TelnyxAgentListResponse", "Data"]


class Data(BaseModel):
    created_at: datetime

    run_id: str

    telnyx_agent_id: str


class TelnyxAgentListResponse(BaseModel):
    data: List[Data]

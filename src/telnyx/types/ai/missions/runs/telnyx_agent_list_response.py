# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ....._models import BaseModel
from .telnyx_agent_data import TelnyxAgentData

__all__ = ["TelnyxAgentListResponse"]


class TelnyxAgentListResponse(BaseModel):
    data: List[TelnyxAgentData]

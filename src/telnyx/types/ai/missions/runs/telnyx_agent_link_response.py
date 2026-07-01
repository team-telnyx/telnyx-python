# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._models import BaseModel
from .telnyx_agent_data import TelnyxAgentData

__all__ = ["TelnyxAgentLinkResponse"]


class TelnyxAgentLinkResponse(BaseModel):
    data: TelnyxAgentData

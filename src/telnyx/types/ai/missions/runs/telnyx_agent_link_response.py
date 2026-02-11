# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ....._models import BaseModel

__all__ = ["TelnyxAgentLinkResponse", "Data"]


class Data(BaseModel):
    created_at: datetime

    run_id: str

    telnyx_agent_id: str


class TelnyxAgentLinkResponse(BaseModel):
    data: Data

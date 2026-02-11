# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["EventListResponse"]


class EventListResponse(BaseModel):
    event_id: str

    run_id: str

    summary: str

    timestamp: datetime

    type: Literal[
        "status_change",
        "step_started",
        "step_completed",
        "step_failed",
        "tool_call",
        "tool_result",
        "message",
        "error",
        "custom",
    ]

    agent_id: Optional[str] = None

    idempotency_key: Optional[str] = None

    payload: Optional[Dict[str, object]] = None

    step_id: Optional[str] = None

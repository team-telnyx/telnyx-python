# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime

from .event_type import EventType
from ....._models import BaseModel

__all__ = ["EventData"]


class EventData(BaseModel):
    event_id: str

    run_id: str

    summary: str

    timestamp: datetime

    type: EventType

    agent_id: Optional[str] = None

    idempotency_key: Optional[str] = None

    payload: Optional[Dict[str, object]] = None

    step_id: Optional[str] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .event_type import EventType

__all__ = ["EventLogParams"]


class EventLogParams(TypedDict, total=False):
    mission_id: Required[str]

    summary: Required[str]

    type: Required[EventType]

    agent_id: str

    idempotency_key: str
    """Prevents duplicate events on retry"""

    payload: Dict[str, object]

    step_id: str

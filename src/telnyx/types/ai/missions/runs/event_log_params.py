# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EventLogParams"]


class EventLogParams(TypedDict, total=False):
    mission_id: Required[str]

    summary: Required[str]

    type: Required[
        Literal[
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
    ]

    agent_id: str

    idempotency_key: str
    """Prevents duplicate events on retry"""

    payload: Dict[str, object]

    step_id: str

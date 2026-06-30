# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["EventType"]

EventType: TypeAlias = Literal[
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

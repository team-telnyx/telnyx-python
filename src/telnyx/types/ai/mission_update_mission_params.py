# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["MissionUpdateMissionParams"]


class MissionUpdateMissionParams(TypedDict, total=False):
    description: str

    execution_mode: "ExecutionMode"

    instructions: str

    metadata: Dict[str, object]

    model: str

    name: str


from .execution_mode import ExecutionMode

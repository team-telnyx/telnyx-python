# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PlanAddStepsToPlanParams", "Step"]


class PlanAddStepsToPlanParams(TypedDict, total=False):
    mission_id: Required[str]

    steps: Required[Iterable[Step]]


class Step(TypedDict, total=False):
    description: Required[str]

    sequence: Required[int]

    step_id: Required[str]

    metadata: Dict[str, object]

    parent_step_id: str

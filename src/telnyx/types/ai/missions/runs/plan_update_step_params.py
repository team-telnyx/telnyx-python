# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PlanUpdateStepParams"]


class PlanUpdateStepParams(TypedDict, total=False):
    mission_id: Required[str]

    run_id: Required[str]

    metadata: Dict[str, object]

    status: Literal["pending", "in_progress", "completed", "skipped", "failed"]

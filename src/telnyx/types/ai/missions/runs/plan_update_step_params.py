# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .step_status import StepStatus

__all__ = ["PlanUpdateStepParams"]


class PlanUpdateStepParams(TypedDict, total=False):
    mission_id: Required[str]

    run_id: Required[str]

    metadata: Dict[str, object]

    status: StepStatus

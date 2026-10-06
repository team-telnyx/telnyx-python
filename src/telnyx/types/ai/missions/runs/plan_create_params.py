# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PlanCreateParams"]


class PlanCreateParams(TypedDict, total=False):
    mission_id: Required[str]

    steps: Required[Iterable["CreatePlanStepRequestParam"]]


from .create_plan_step_request_param import CreatePlanStepRequestParam

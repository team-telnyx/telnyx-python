# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["MetricRetrieveGenerateMetricsProgressResponse", "Metric"]


class Metric(BaseModel):
    agent: Optional[int] = None

    description: Optional[str] = None

    eval_type: Optional[str] = None

    name: Optional[str] = None

    scenarios: Optional[List[int]] = None


class MetricRetrieveGenerateMetricsProgressResponse(BaseModel):
    agent_id: int

    current_step: str

    error: Optional[str] = None

    metrics: List[Metric]

    status: Literal["queued", "processing", "completed", "failed"]

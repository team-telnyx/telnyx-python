# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime

from ......_models import BaseModel

__all__ = ["ResultListResponse", "Result", "ResultRun", "ResultScenario"]


class ResultRun(BaseModel):
    id: Optional[int] = None

    inbound_number: Optional[str] = None

    number: Optional[str] = None

    scenario: Optional[int] = None

    scenario_name: Optional[str] = None

    status: Optional[str] = None


class ResultScenario(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class Result(BaseModel):
    id: int

    agent: int

    created_at: datetime

    name: str

    status: str
    """
    Run batch status: running, completed, failed, pending, in_progress, evaluating,
    in_queue, timeout, cancelled, or scaling_up.
    """

    updated_at: datetime

    agent_inbound: Optional[bool] = None

    agent_name: Optional[str] = None

    completed_runs_count: Union[int, str, None] = None

    failed_runs_count: Union[int, str, None] = None

    is_cronjob: Optional[bool] = None
    """Whether this batch was started by a scheduled job."""

    met_expected_outcome_count: Union[int, str, None] = None

    run_as_text: Optional[bool] = None
    """Whether the batch ran as text chat rather than voice calls."""

    run_type: Optional[str] = None

    runs: Optional[List[ResultRun]] = None
    """Run summaries in this batch. Retrieve the batch for detail keyed by run ID."""

    scenarios: Optional[List[ResultScenario]] = None

    success_rate: Union[float, str, None] = None
    """Share of runs judged successful."""

    success_runs_count: Union[int, str, None] = None

    total_expected_outcome_count: Union[int, str, None] = None

    total_runs_count: Union[int, str, None] = None


class ResultListResponse(BaseModel):
    next: Optional[str] = None

    previous: Optional[str] = None

    results: List[Result]

    count: Optional[int] = None

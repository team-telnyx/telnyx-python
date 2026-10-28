# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime

from ......_models import BaseModel

__all__ = ["TestRunResult", "Runs", "RunsScenario", "Scenario"]


class RunsScenario(BaseModel):
    id: Optional[int] = None

    expected_outcome_prompt: Optional[str] = None

    name: Optional[str] = None

    personality_name: Optional[str] = None


class Runs(BaseModel):
    id: Optional[int] = None

    duration: Optional[str] = None

    error_message: Optional[str] = None

    evaluation_status: Optional[str] = None

    executed_at: Optional[str] = None

    personality_name: Optional[str] = None

    scenario: Optional[RunsScenario] = None

    scenario_name: Optional[str] = None

    status: Optional[str] = None

    success: Optional[bool] = None

    test_profile_name: Optional[str] = None

    timestamp: Optional[str] = None


class Scenario(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class TestRunResult(BaseModel):
    __test__ = False
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

    runs: Optional[Dict[str, Runs]] = None
    """Per-run detail keyed by run ID."""

    scenarios: Optional[List[Scenario]] = None

    success_rate: Union[float, str, None] = None
    """Share of runs judged successful."""

    success_runs_count: Union[int, str, None] = None

    total_expected_outcome_count: Union[int, str, None] = None

    total_runs_count: Union[int, str, None] = None

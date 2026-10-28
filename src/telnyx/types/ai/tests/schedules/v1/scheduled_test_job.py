# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["ScheduledTestJob", "ScenariosData"]


class ScenariosData(BaseModel):
    id: Optional[int] = None

    agent: Optional[int] = None

    name: Optional[str] = None

    personality: Optional[int] = None

    personality_name: Optional[str] = None


class ScheduledTestJob(BaseModel):
    id: int

    agent: int
    """ID of the test agent the job belongs to."""

    created_at: datetime

    crontab_expression: str
    """Cron expression controlling when the job runs, in the job's timezone."""

    is_active: bool

    name: str

    updated_at: datetime

    execution_mode: Optional[str] = None
    """Execution mode for the test runs, such as voice, text, or sip."""

    frequency: Optional[int] = None

    notify_on: Optional[Literal["never", "success", "failure", "both"]] = None
    """When the job sends a notification."""

    personalities: Optional[List[int]] = None

    personality: Optional[int] = None

    run_as_text: Optional[bool] = None
    """Whether the job runs scenarios as text chat rather than voice calls."""

    scenario_ids: Optional[List[int]] = None
    """Scenario IDs the job executes."""

    scenarios_data: Optional[List[ScenariosData]] = None

    tags: Optional[List[str]] = None

    timezone: Optional[str] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ......_types import SequenceNotStr

__all__ = ["CronJobCronJobsParams"]


class CronJobCronJobsParams(TypedDict, total=False):
    crontab_expression: Required[str]
    """Cron expression controlling when the job runs."""

    agent: int

    execution_mode: str
    """Execution mode for the test runs, such as voice, text, or sip."""

    frequency: int

    is_active: bool

    name: str

    notify_on: Literal["never", "success", "failure", "both"]

    personalities: Iterable[int]

    run_as_text: bool

    scenarios: Iterable[int]

    tags: SequenceNotStr[str]

    timezone: str

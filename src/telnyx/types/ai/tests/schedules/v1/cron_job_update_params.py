# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from ......_types import SequenceNotStr

__all__ = ["CronJobUpdateParams"]


class CronJobUpdateParams(TypedDict, total=False):
    agent: Optional[int]

    crontab_expression: str
    """Cron expression controlling when the job runs."""

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

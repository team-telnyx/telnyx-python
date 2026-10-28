# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

from .scheduled_test_job import ScheduledTestJob

__all__ = ["CronJobRetrieveCronJobsResponse"]

CronJobRetrieveCronJobsResponse: TypeAlias = List[ScheduledTestJob]

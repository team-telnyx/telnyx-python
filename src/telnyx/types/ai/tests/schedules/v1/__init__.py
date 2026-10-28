# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .cron_job_update_params import CronJobUpdateParams as CronJobUpdateParams
from .cron_job_cron_jobs_params import CronJobCronJobsParams as CronJobCronJobsParams
from .cron_job_retrieve_cron_jobs_params import CronJobRetrieveCronJobsParams as CronJobRetrieveCronJobsParams
from .cron_job_retrieve_cron_jobs_response import CronJobRetrieveCronJobsResponse as CronJobRetrieveCronJobsResponse

if TYPE_CHECKING:
    from .scheduled_test_job import ScheduledTestJob as ScheduledTestJob


def __getattr__(name: str) -> Any:
    if name == "ScheduledTestJob":
        from .scheduled_test_job import ScheduledTestJob

        return ScheduledTestJob
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

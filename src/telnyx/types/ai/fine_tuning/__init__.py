# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .job_create_params import JobCreateParams as JobCreateParams

if TYPE_CHECKING:
    from .fine_tuning_job import FineTuningJob as FineTuningJob
    from .job_list_response import JobListResponse as JobListResponse


def __getattr__(name: str) -> Any:
    if name == "FineTuningJob":
        from .fine_tuning_job import FineTuningJob

        return FineTuningJob
    if name == "JobListResponse":
        from .job_list_response import JobListResponse

        return JobListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

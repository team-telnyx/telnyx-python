# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .job_list_params import JobListParams as JobListParams
from .job_delete_phone_number_block_params import JobDeletePhoneNumberBlockParams as JobDeletePhoneNumberBlockParams

if TYPE_CHECKING:
    from .job import Job as Job
    from .job_error import JobError as JobError
    from .job_retrieve_response import JobRetrieveResponse as JobRetrieveResponse
    from .job_delete_phone_number_block_response import (
        JobDeletePhoneNumberBlockResponse as JobDeletePhoneNumberBlockResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "Job":
        from .job import Job

        return Job
    if name == "JobError":
        from .job_error import JobError

        return JobError
    if name == "JobRetrieveResponse":
        from .job_retrieve_response import JobRetrieveResponse

        return JobRetrieveResponse
    if name == "JobDeletePhoneNumberBlockResponse":
        from .job_delete_phone_number_block_response import JobDeletePhoneNumberBlockResponse

        return JobDeletePhoneNumberBlockResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

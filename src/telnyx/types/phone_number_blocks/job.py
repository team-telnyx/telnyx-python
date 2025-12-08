# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .job_error import JobError

__all__ = ["Job", "FailedOperation", "SuccessfulOperation"]


class FailedOperation(BaseModel):
    id: Optional[str] = None
    """The phone number's ID"""

    errors: Optional[List[JobError]] = None

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class SuccessfulOperation(BaseModel):
    """The phone numbers successfully updated."""

    id: Optional[str] = None
    """The phone number's ID"""

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class Job(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    etc: Optional[datetime] = None
    """
    ISO 8601 formatted date indicating when the estimated time of completion of the
    background job.
    """

    failed_operations: Optional[List[FailedOperation]] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    status: Optional[Literal["pending", "in_progress", "completed", "failed"]] = None
    """Indicates the completion status of the background operation."""

    successful_operations: Optional[List[SuccessfulOperation]] = None

    type: Optional[Literal["delete_phone_number_block"]] = None
    """Identifies the type of the background job."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""
